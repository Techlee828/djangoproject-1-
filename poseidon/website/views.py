from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime
from valve.models import Valve
from manual.forms import ManualForm
#from valve.forms import Valveform

def welcome(request):


    return render(request, "website/welcome.html",
             {"current_time" : datetime.now(),   # this is a "dictionary"
             "valves" : Valve.objects.all(),
             "num_valves" : Valve.objects.count(),

              }
)


