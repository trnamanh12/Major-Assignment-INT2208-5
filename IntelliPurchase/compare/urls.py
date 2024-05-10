from django.urls import path
from . import views

urlpatterns = [
   path('', views.compare, name='compare'),
   path('search/', views.search, name='search'),
   path('save_history/', views.save_history, name='save_history'),
]