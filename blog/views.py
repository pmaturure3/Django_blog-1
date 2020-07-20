from django.views import generic
from .models import Post
from django.shortcuts import render, redirect

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")