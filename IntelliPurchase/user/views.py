from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register(request):
    form = CreateUserForm()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'users/register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect!')
    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
