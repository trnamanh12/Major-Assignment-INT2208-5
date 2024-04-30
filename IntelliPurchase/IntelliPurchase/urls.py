"""
URL configuration for IntelliPurchase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.authors, name='authors'),
    path('account/', views.account, name='account'),
    path('account/link_phone/', views.link_phone, name='link_phone'),
    path('account/link_email/', views.link_email, name='link_email'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/delete/', views.delete_product, name='delete_product'),
    path('product/compare/', views.compare_products, name='compare_products'),
    path('product/compare_specs/', views.compare_specs, name='compare_specs'),
    path('product/compare_prices/', views.compare_prices, name='compare_prices'),
    path('product/compare_ratings/', views.compare_ratings, name='compare_ratings'),
    path('seller/', views.seller, name='seller'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user/favorites/', views.user_favorites, name='user_favorites'),
    path('admin/', admin.site.urls),
    path('home', include('home.urls')),
    path('blog/', include('blog.urls')),
]

handler404 = 'home.views.error'

