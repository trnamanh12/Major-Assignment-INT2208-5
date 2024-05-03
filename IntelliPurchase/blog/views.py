from django.shortcuts import render
from .models import Product, Post
from django.views.generic import ListView, DetailView

# Create your views here.
# def list(request):
#     Data = {'Products': Product.objects.all().order_by('-product_id')}
#     return render(request, 'blog/blog.html', Data)

class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = 'blog/blog.html'
    context_object_name = 'Posts'
    paginate_by = 1

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'