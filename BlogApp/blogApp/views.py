from django.shortcuts import render

from blogApp.models import BlogDetails

def blogList(request):
    blogs = BlogDetails.objects.all().values()
    return render(request,'blog_list.html',{'blogs' : blogs})

# def home(request):
#     return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

# def blog(request):
#     return render(request, 'blog.html')

# def contact(request):
#     return render(request, 'contact.html')

# def categories(request):
#     return render(request, 'categories.html')

# def search(request):
#     return render(request, 'search.html')

# def privacy_policy(request):
#     return render(request, 'privacy_policy.html')

# def social_media_links(request):
#     return render(request, 'social_media_links.html')

