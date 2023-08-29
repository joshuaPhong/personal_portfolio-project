from django.shortcuts import render
from .models import BlogModel


# Create your views here.

def all_blogs(request):
    blog_object = BlogModel.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogObject': blog_object})
