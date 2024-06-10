from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField() # Nom transformé à utiliser dans les url
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()
    