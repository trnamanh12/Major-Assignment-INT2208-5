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

from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post": post, "form": form})

