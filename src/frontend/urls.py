

from django.urls import path
from frontend.views import index, blog


urlpatterns = [
    path("", index, name="home"),
    path("blog/", blog, name="blog")
]
