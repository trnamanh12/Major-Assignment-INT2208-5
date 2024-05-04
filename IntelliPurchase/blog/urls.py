from django.urls import path
from .models import Post
from . import views
from django.views.generic import ListView

urlpatterns = [
   path('', ListView.as_view(
      queryset = Post.objects.all().order_by('-date'),
      template_name = 'blog/blog.html',
      context_object_name = 'Posts',
      paginate_by = 1)
      , name='blog'),
   path('<int:pk>/', views.post, name='post'),
]