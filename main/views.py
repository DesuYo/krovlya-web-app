from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models

def render_home(req):
    products = models.ProductModel.objects.all()
    slides = models.SlideModel.objects.all()
    return render(req, 'home.html', { 'slides': slides, 'products': products })