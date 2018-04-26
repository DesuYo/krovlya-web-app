from django.shortcuts import render, get_object_or_404
from . import models

def render_home(req):
    products = models.ProductModel.objects.all()
    slides = models.SlideModel.objects.all()
    contacts = models.ContactModel.objects.all()
    return render(req, 'home.html', { 'slides': slides, 'products': products, 'contacts': contacts })

def render_product_page(req, id=None):
    products = models.ProductModel.objects.all()
    product = get_object_or_404(models.ProductModel, slug=id)
    contacts = models.ContactModel.objects.all()
    return render(req, 'product.html', { 'products': products, 'product': product, 'contacts': contacts })

def render_contacts_page(req):
    products = models.ProductModel.objects.all()
    contacts = models.ContactModel.objects.all()
    return render(req, 'contacts.html', { 'products': products, 'contacts': contacts })