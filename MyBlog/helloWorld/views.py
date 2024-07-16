from django.shortcuts import render
# Create your views here.

def viewsHello(responce):
    return render(responce,"hello.html")