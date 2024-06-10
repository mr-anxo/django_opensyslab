import json
from blog.models import BlogPost

with open("blog/static/tools/blog-blogpost.json","r") as file:
    data = json.load(file)

for bp in data:
    BlogPost.objects.create(title=bp["title"],
                            slug=bp["slug"],
                            published=bp["published"],
                            content=bp["content"],
                            description=bp["description"],
                            url=bp["url"],
                            date=bp["date"])