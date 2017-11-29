from django.shortcuts import render
from app.models import *

# Create your views here.

def main(request):
    return render(request, 'MainPage.html',{})

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
