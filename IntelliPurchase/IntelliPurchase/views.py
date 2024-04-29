from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def account(request):
    return render(request, "account.html")

def authors(request):
    return render(request, "authors.html")

def compare_prices(request):
    return render(request, "compare_prices.html")

def compare_products(request):
    return render(request, "compare_products.html")

def compare_ratings(request):
    return render(request, "compare_ratings.html")

def compare_specs(request):
    return render(request, "compare_specs.html")

def link_phone(request):
    return render(request, "link_phone.html")

def link_email(request):
    return render(request, "link_email.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def seller(request):
    return render(request, "seller.html")

def user_favorites(request):
    return render(request, "user_favorites.html")

def add_product(request):
    return render(request, "add_product.html")

def delete_product(request):
    return render(request, "delete_product.html")
