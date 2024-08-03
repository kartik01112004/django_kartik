from django.shortcuts import render
from .models import BlogDetails

def blog_list(request):
    blogs = BlogDetails.objects.all().values()
    return render(request, 'blog_list.html', {'blogs': blogs})