from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from haystack.forms import ModelSearchForm
from django.core import serializers
import json
from app.models import *
from utils import sendEmail

# Create your views here.

def main(request):
    return render(request, 'MainPage.html',{'form':ModelSearchForm})

def enzyme_page(request,label):
    try:
        ec = Enzyme.objects.get(label=label)
    except:
        pass
    return_form = {'ec':ec}
    return render(request, 'EnzymeFileTemplate.html',return_form)

def cofactors_list(request):
    cofs = Cofactor.objects.distinct('cofactor')
    return_form = {'cofs':cofs}
    return render(request,'cofactorList.html',return_form)

def cofactors_page(request,cofactor):
    try:
        ecs = Cofactor.objects.filter(cofactor=cofactor)
    except:
        pass
    return_form = {'cof':cofactor,'ecs':ecs}
    return render(request, 'cofactorPage.html',return_form)

def send_bug(request):
    if request.method == 'POST':
        data={k: v[0] if len(v) == 1 else v for k, v in request.POST.lists()}
        sendEmail(txt='bugEmail.txt',html='bugEmail.html',data=data,
                title='[Bug Report]'+data['subject'],to=['hua-ting.yao@u-psud.fr'])

def timeline(request):
    return render(request, 'timeline.html',{})

def timelineData(request):
    if request.method == 'GET':
        data = {}
        # data['result'] = []
        events = TimelineEvent.objects.order_by('?')[:100]
        data['events'] = json.loads(serializers.serialize('json', events))
        #data['events'] = events
        return  HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponseRedirect('/')
