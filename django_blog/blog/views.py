from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = Post.objects.all()

# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = { 'title': 'About'}
    return render(request, 'blog/about.html', context)
