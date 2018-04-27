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

class PromotionModel(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextField()
    image = models.ImageField(default='default.png')
    createdAt = models.DateField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    value = models.CharField(max_length=30)
    iconName = models.SlugField(max_length=25)
    createdAt = models.DateField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.value

class DeliveryModel(models.Model): 
    title = models.CharField(max_length=30)
    subTitle = models.CharField(max_length=50)
    thumbnail = models.ImageField(default='default.png')
    description = RichTextField()
    createdAt = models.DateField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

class AdvantageModel(models.Model):
    title = models.CharField(max_length=30)
    subTitle = models.CharField(max_length=50)
    createdAt = models.DateField(auto_now=False, auto_now_add=True)
    updatedAt = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

