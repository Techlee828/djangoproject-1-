
from django.shortcuts import render,redirect

from django.http import HttpResponse

from .forms import ManualForm





def valvestate(request):
    if request.method == 'POST':
        form = request.POST.get('textfield', None)



        return redirect("/welcome")    # redirects user to welcome page after hitting submit

        #if form.is_valid():

        print('textfield')



            #name = form.cleaned_data['name']
    else:
        form = ManualForm()


    return render(request, 'form.html', { 'form': form })

# Create your views here.
