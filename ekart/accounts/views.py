from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'account/login.html')

def logout():
    pass


def register(request):
    return render(request, 'account/register.html')
