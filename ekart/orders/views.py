from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Featured_Product
from orders.models import Order

@login_required
def buy_now(request, product_id):
    product = Featured_Product.objects.get(id=product_id)
    # Here you would create an order and handle payment
    order = Order.objects.create(user=request.user, product=product, confermed=False)
    order.save()
    return redirect('order_confirmation', order_id=order.id)

@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})
