from django.contrib import admin
from .models import ProductModel, PromotionModel, ContactModel, DeliveryModel

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'textPreview', 'content']

    class Meta:
        model = ProductModel

class PromotionModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'description']

    class Meta:
        model = PromotionModel

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['value', 'createdAt', 'updatedAt']
    search_fields = ['value', 'iconName']

    class Meta:
        model = ContactModel

class DeliveryModelAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'createdAt', 'updatedAt']
    search_fields = ['title', 'subTitle', 'description']

    class Meta:
        model = DeliveryModel
        verbose_name = 'Deliveries'

admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(PromotionModel, PromotionModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
admin.site.register(DeliveryModel, DeliveryModelAdmin)
