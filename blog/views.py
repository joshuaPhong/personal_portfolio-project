from django.shortcuts import render, get_object_or_404
from .models import BlogModel


# Create your views here.

def all_blogs(request):
    # we can set limits slice the blog object
    # and order by reverse date (newest first).
    blog_object = BlogModel.objects.order_by('-date')[0:5]
    # blog_object = BlogModel.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogObject': blog_object})


def detail(request, blog_id):
    # grabs the blogid from the blog model or returns a 404
    blog = get_object_or_404(BlogModel, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
