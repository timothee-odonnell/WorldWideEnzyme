from django.shortcuts import render
from app.models import *

# Create your views here.

def main(request):
    return render(request, 'MainPage.html','')

def enzyme_page(request):
    return render(request, 'EnzymeFileTemplate.html','')
