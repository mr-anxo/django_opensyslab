from django.http import HttpResponse
from django.shortcuts import render

from blog.models import BlogPost

# Create your views here.

def index(request):
    return HttpResponse("Hello World !")

def article(request,article_number):
    articles = BlogPost.objects.get(id=article_number)
    if 1 <= article_number <= 3:
        return render(request, f"article.html", context={ "article" : article})
    else:
        return render(request, "404.html")
       