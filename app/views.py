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
