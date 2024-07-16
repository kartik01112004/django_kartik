from django.shortcuts import render

# Create your views here.
def viewIndex(response):
    return render(response, "index.html")
