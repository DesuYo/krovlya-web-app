from django.shortcuts import render, get_object_or_404
from django.urls import resolve
from . import models

def retrieveUsefullStuff(req):
    products = models.ProductModel.objects.all()
    contacts = models.ContactModel.objects.all()
    return { 'url': req.path_info, 'products': products, 'contacts': contacts }

def render_home(req):
    promotions = models.PromotionModel.objects.all()
    deliveries = models.DeliveryModel.objects.all()
    options = { 'promotions': promotions, 'deliveries': deliveries }
    options.update(retrieveUsefullStuff(req))
    return render(req, 'home.html', options)

def render_product_page(req, id=None):
    product = get_object_or_404(models.ProductModel, slug=id)
    options = { 'product': product }
    options.update(retrieveUsefullStuff(req))
    return render(req, 'product.html', options)

def render_contacts_page(req):
    page = get_object_or_404(models.SimplePageModel, slug='about_us')
    options = { 'page': page }
    options.update(retrieveUsefullStuff(req))
    return render(req, 'about_us.html', options)

def render_simple_page(req, id=None): 
    page = get_object_or_404(models.SimplePageModel, slug=id)
    options = { 'page': page }
    options.update(retrieveUsefullStuff(req))
    return render(req, 'simple.html', options)