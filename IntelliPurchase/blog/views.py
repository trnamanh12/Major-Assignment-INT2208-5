from django.shortcuts import render
from .models import Product, Post
# Create your views here.
# def list(request):
#     Data = {'Products': Product.objects.all().order_by('-product_id')}
#     return render(request, 'blog/blog.html', Data)
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})