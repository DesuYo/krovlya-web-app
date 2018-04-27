from django.contrib import admin
from . import models

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'textPreview', 'content']

    class Meta:
        model = models.ProductModel

class PromotionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'description']

    class Meta:
        model = models.PromotionModel

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['value', 'createdAt', 'updatedAt']
    search_fields = ['value', 'iconName']

    class Meta:
        model = models.ContactModel

class DeliveryModelAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'subTitle', 'description']

    class Meta:
        model = models.DeliveryModel
        verbose_name = 'Deliveries'

class SimplePageModelAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'content']

    class Meta:
        model = models.SimplePageModel

admin.site.register(models.ProductModel, ProductModelAdmin)
admin.site.register(models.PromotionModel, PromotionModelAdmin)
admin.site.register(models.ContactModel, ContactModelAdmin)
admin.site.register(models.DeliveryModel, DeliveryModelAdmin)
admin.site.register(models.SimplePageModel, SimplePageModelAdmin)
