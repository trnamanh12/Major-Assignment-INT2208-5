from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   return render(request, 'lichsugia.com/index.html')

def contact(request):
   return render(request, 'contact.html')

def error(request, exception):
   return render(request, 'error.html', {'message': exception})

def test(request):
   return render(request, 'test.html')
