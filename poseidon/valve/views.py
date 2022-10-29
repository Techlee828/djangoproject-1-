from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ValveForm
from subprocess import Popen
#from valve import pyfirm

def new(request):
    if request.method == "POST":
        form = ValveForm(request.POST)
        form.save()   # can add if valid command here to verify data that is imput from user
        #if request .POST["on"]: # if on = "true"  aka box is checked
       # Popen("pyfirm.py")
        print('The POST data is : ', request.POST)

        return HttpResponse("your valve should be turning on now POST %s")
        p = Popen("pyfirm.py", "prints a value")

     #   return render(request, "website/welcome.html")
    else:
        form =  ValveForm()
        print('The request method is: ', request.method)
        print('The POST data is : ', request.POST)

        #return HttpResponse("welp i hope this works  GET %s")

        return render(request, "valve/new.html", {"form" : form})


# Create your views here.
def command(request):
    context = {
        "title" : "Trigger Pyfirmata"
    }

    return redirect("/")

def commandposeidon(request):
    print("\n This is me printing on command\n")

    return HttpResponse("""""")
