from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog

def all_blogs(request):
    #blog_objs = Blog.objects.all()
    blog_objs = Blog.objects.order_by('-date') # Most recent first
    return render(request, 'blog/all_blogs.html', {'blogs': blog_objs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # pk = primary key
    return render(request, 'blog/detail.html', {'blog': blog})
