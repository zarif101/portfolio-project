from django.shortcuts import render, get_object_or_404
from .models import blogpost
# Create your views here.

def allblogs(request):
    blogposts = blogpost.objects
    return render(request, 'blog/allblogs.html', {'blogpost':blogposts})

def detailpost(request, blog_id):
    detailblog = get_object_or_404(blogpost, pk=blog_id)
    return render(request, 'blog/detailed.html', {'detailblog':detailblog})
