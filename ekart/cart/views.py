# orders/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Featured_Product
from .models import Cart, CartItem
from orders.models import Order
from orders.views import order_confirmation, buy_now
import uuid
from django.urls import reverse

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Featured_Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')



# orders/views.py

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    # Handle the checkout process
    # This is a simplified example, you might want to integrate with a payment gateway
    if request.method == 'POST':
        order_id = uuid.uuid4()
        for item in cart_items:
            # Create an order for each item

            Order.objects.create(user=request.user, product=item.product, order_id=order_id)
        # Clear the cart
        cart_items.delete()
        return redirect(reverse(order_confirmation, kwargs={'order_id': order_id}))

    return render(request, 'cart/checkout.html', {'cart_items': cart_items})
