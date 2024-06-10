from django.db import models
from django.utils.text import slugify
from datetime import date

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField() # Nom transformé à utiliser dans les url
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()
    url = models.URLField(max_length=512,default="https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        if not self.date and self.published:
            self.date = date.today()
            
        super().save(*args, **kwargs)
    