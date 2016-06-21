from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import DepChamber
from .models import FacePlate
from .models import UpperBlockerPlate
from .models import LowerBlockerPlate
from .models import PedestalHeater
from .models import TopTuner
from .models import BottomTuner
from .models import OtherParts
from .models import GasBox

# Create your views here.

def HW_home(request):
	#dc1=get_object_or_404(DepChamber, id=1)
	depCham_list=DepChamber.objects.all()
	context={
		"title": "List",
		"object_list":depCham_list
	}
	return render(request,"index.html",context)
    #return HttpResponse("HW home page.")

def index(request):
    foup_list=Foup.objects.all()
    template=loader.get_template('runsheet/index.html')
    context={'foup_list':foup_list,}
    return HttpResponse(template.render(context,request))

def Foup_detail(request,Foup_name):
    if Foup_name[0]=='F' or Foup_name[0]=='f':
        Foup_name=Foup_name[1:len(Foup_name)]

    return HttpResponse("You are looking at the Foup %s." % Foup_name)
