from django.urls import path
from products import views


urlpatterns = [
    path('clothes/', views.get_all_products, name='all_products'),
]
