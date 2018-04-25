from django.shortcuts import render, get_object_or_404
from . import models

def render_home(req):
    products = models.ProductModel.objects.all()
    slides = models.SlideModel.objects.all()
    return render(req, 'home.html', { 'slides': slides, 'products': products })

def render_product_page(req, id=None):
    products = models.ProductModel.objects.all()
    product = get_object_or_404(models.ProductModel, slug=id)
    return render(req, 'product.html', { 'products': products, 'product': product })