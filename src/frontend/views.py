from django.shortcuts import render
from blog.models import BlogPost


# Create your views here.

def index(request):
    return render(request, "index.html")

def blog(request):
    articles = BlogPost.objects.all().filter(published=True)
    return render(request, "blog.html",context={ "articles" : articles})