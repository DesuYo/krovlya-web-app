from django.contrib import admin
from .models import ProductModel, SlideModel, ContactModel

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'textPreview', 'content']

    class Meta:
        model = ProductModel

class SlideModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'description']

    class Meta:
        model = ProductModel

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['value', 'createdAt', 'updatedAt']
    search_fields = ['value', 'iconName']

    class Meta:
        model = ContactModel

admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(SlideModel, SlideModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
