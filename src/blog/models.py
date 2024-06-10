from django.db import models
from django.utils.text import slugify

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField() # Nom transformé à utiliser dans les url
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify()
        
        if not self.date and self.published:
            self.date = 
        super().save(*args, **kwargs)
    