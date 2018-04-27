from django.shortcuts import render, get_object_or_404
from . import models

def render_home(req):
    products = models.ProductModel.objects.all()
    promotions = models.PromotionModel.objects.all()
    contacts = models.ContactModel.objects.all()
    deliveries = models.DeliveryModel.objects.all()
    return render(req, 'home.html', { 'promotions': promotions, 'products': products, 'contacts': contacts, 'deliveries': deliveries })

def render_product_page(req, id=None):
    products = models.ProductModel.objects.all()
    product = get_object_or_404(models.ProductModel, slug=id)
    contacts = models.ContactModel.objects.all()
    return render(req, 'product.html', { 'products': products, 'product': product, 'contacts': contacts })

def render_contacts_page(req):
    products = models.ProductModel.objects.all()
    contacts = models.ContactModel.objects.all()
    return render(req, 'about.html', { 'products': products, 'contacts': contacts })