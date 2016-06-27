from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from sets import Set
# Create your views here.

def index(request):
##    foup_list=Foup.objects.all()
##    template=loader.get_template('runsheet/index.html')
##    context={'foup_list':foup_list,}
    return HttpResponse( "you are at foup homepage.")
    #return HttpResponse(template.render(context,request))

##def Foup_detail(request,Foup_name):
##    if Foup_name[0]=='F' or Foup_name[0]=='f':
##        Foup_name=Foup_name[1:len(Foup_name)]
##
##    return HttpResponse("You are looking at the Foup %s." % Foup_name)
##
##def Foup_home(request):
##    foup_slot_list=Foup_slot.objects.all()
##    foup_set=Set()
##    for slot in foup_slot_list:
##        foup_set.add(slot.foup)
##    foup_list=list(foup_set)
##    context={
##        "title":"Foup List:",
##        "foup_list":foup_list,
##    }
##    return render(request,"Foup_index.html",context)