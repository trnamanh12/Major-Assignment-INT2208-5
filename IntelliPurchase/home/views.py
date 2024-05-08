from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   return render(request, 'home.html')

def contact(request):
   return render(request, 'contact.html')

def error(request, exception):
   return render(request, 'error.html', {'message': exception})

from .forms import RegistrationForm
from django.http import HttpResponseRedirect 

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form': form})