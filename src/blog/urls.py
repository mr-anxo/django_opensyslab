

from django.urls import path
from blog.views import article, index


urlpatterns = [
    #path("article<int:article_number>/", article, name="article"),
    path("article/<str:article_slug>", article, name="article")
]
