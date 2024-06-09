from django.shortcuts import render
from products.models import Featured_Product
# Create your views here.
def get_all_products():
    all_products = Featured_Product.objects.all()
    return all_products