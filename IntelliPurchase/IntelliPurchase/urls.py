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
from home import views
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
from user import views as user_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('compare/', include('compare.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.loginUser, name='login'),
    path('logout/', user_views.logoutUser, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.error'

