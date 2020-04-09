from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from register.models import Place
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def wt_home(request):
	return render(request,'wt_home1.html')
def log(request):
	return render(request,'login_template.html')
def home(request):
	return render(request,'wt_home1.html')
def base(request):
	return render(request,'wt_base.html')

def search_titles(request,):
    print("inside search_titles")

    if(request.method=="POST"):
        search_text=request.POST.get('search_text')
        print(search_text)
    else:
        search_text=''
    valid=Place.objects.filter(place__contains= search_text)
    
    print("searching ", search_text)
    print("valid :",valid)
    return render(request,'ajax_search.html',{'skills':valid})
    


