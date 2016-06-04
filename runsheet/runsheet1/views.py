from django.shortcuts import render
from django.http import HttpResponse
from .models import Foup
from django.template import loader

# Create your views here.

def index(request):
    foup_list=Foup.objects.all()
    template=loader.get_template('runsheet/index.html')
    context={'foup_list':foup_list,}
    return HttpResponse(template.render(context,request))

def Foup_detail(request,Foup_name):
    if Foup_name[0]=='F' or Foup_name[0]=='f':
        Foup_name=Foup_name[1:len(Foup_name)]

    return HttpResponse("You are looking at the Foup %s." % Foup_name)
