from django.shortcuts import render
from .models import Blog


def blogPage(request):
    my_blogs = Blog.objects
    return render(request, 'blog.html', {'blogs': my_blogs})
