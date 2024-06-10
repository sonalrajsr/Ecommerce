from django.shortcuts import render, get_object_or_404
from products.models import Featured_Product
# Create your views here.
def get_all_products():
    all_products = Featured_Product.objects.all()
    return all_products

def product_detail(request, product_id):
    product = get_object_or_404(Featured_Product, id = product_id)
    return render(request, 'product.html', {'product' : product})