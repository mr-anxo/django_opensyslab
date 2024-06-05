

from django.urls import path
from blog.views import article, index


urlpatterns = [
    #path("", index, name=""),
    path("article<int:article_number>/", article, name="article")
]
