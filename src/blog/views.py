from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogPost

# Create your views here.

def index(request):
    return HttpResponse("Hello World !")

def article(request,article_slug):
    article = BlogPost.objects.get(slug=article_slug)
    if article.slug:
        return render(request, f"article.html", context={ "article" : article})
    else:
        return render(request, "404.html")
       