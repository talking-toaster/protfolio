from django.shortcuts import render, get_object_or_404
from .models import Blog


def blogPage(request):
    my_blogs = Blog.objects
    return render(request, 'blog.html', {'blogs': my_blogs})


def blogText(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_text.html', {'blog': blog})
