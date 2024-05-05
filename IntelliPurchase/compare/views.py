from django.shortcuts import render

# Create your views here.
def compare(request):
    return render(request, 'prototype.html')