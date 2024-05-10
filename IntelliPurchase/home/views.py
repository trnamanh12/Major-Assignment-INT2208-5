from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   return render(request, 'lichsugia.com/index.html')

def support(request):
   return render(request, 'lichsugia.com/support.html')

def privacy(request):
   return render(request, 'lichsugia.com/privacy.html')

def terms(request):
   return render(request, 'lichsugia.com/terms.html')

def contact(request):
   return render(request, 'contact.html')

def error(request, exception):
   return render(request, 'error.html', {'message': exception})

