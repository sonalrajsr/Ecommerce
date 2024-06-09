from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ekart.views import home

#login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(home) 
        else:
            return render(request, 'account/Login.html', {'error_message': 'Invalid username or password'})

    # If request method is not POST, render the login page
    return render(request, 'account/Login.html')




#log out view
def logout_view(request):
    logout(request)
    return redirect(home) 



#register view
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        # gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'registration_form.html', {'error_message': 'Passwords do not match'})
        # Create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        # Set additional user fields
        user.save()

        # Redirect to success page or login page
        return redirect('login')
    return render(request, 'account/register.html')
