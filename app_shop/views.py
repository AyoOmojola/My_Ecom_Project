from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app_shop.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'app_shop/home.html'

class ProductDetail(DetailView):
    model = Product
    template_name = 'app_shop/product_detail.html'