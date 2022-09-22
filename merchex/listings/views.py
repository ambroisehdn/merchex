from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
# Create your views here.

def hello(request) :
    bands = Band.objects.all()
    return render(request,"listings/hello.html",{"bands":bands})

def about(request) :
    return render(request=request,template_name="listings/about/index.html")

def contact(request) :
    return render(request=request,template_name="listings/contact/index.html")

def listing(request) :
    bands = Band.objects.all()
    return render(request=request,template_name="listings/hello.html",context={"bands":bands})