from django.urls import path
from products import views


urlpatterns = [
    path('clothes/', views.get_all_products, name='all_products'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
]
