from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'store/products-list.html'
    context_object_name = 'products'
    paginate_by = 20
    def get_queryset(self):
        return Product.objects.filter(available=True)

class HomePage(ListView):
    model = Product
    template_name = 'store/home-page.html'
    context_object_name = 'products'
    paginate_by = 20
class DetailPage(DetailView):
    model = Product
    template_name = 'store/detail-page.html'
    context_object_name = 'product'
