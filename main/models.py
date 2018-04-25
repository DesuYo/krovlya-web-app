from django.db import models
from ckeditor.fields import RichTextField

class ProductModel(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=25)
    thumbnail = models.ImageField(default='default.png')
    textPreview = RichTextField()
    content = RichTextField()
    createdAt = models.DateField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class SlideModel(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextField()
    background = models.ImageField(default='default.png')
    createdAt = models.DateField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
 

