from django.urls import path
from orders import views


urlpatterns = [
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
