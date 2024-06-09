from django.shortcuts import render
from products.models import Featured_Product, New_arrival
def home(request):
    all_featured_products = Featured_Product.objects.all()
    all_new_products = New_arrival.objects.all()
    if request.user.is_authenticated:
        # Get the username of the logged-in user
        username = request.user.username
        # Pass the username to the template context
        return render(
                        request, 
                        'home.html',
                       {
                           'username': username, 
                            'all_featured_products' : all_featured_products,
                            'all_new_products' : all_new_products 
                        }
                    )
    else:
        # Handle the case when the user is not logged in
        return render(request, 'home.html', {'all_featured_products' : all_featured_products,
                            'all_new_products' : all_new_products })
    
def shop(request):
    all_featured_products = Featured_Product.objects.all()
    all_new_products = New_arrival.objects.all()
    return render(
        request, 
        'shop.html',
        {
          'all_featured_products' : all_featured_products,
            'all_new_products' : all_new_products   
        }
    )
