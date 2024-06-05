from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World !")

def article(request,article_number):
    if 1 <= article_number <= 3:
        return render(request, f"article{article_number}.html")
    else:
        return render(request, "404.html")
       