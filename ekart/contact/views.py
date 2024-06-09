from django.shortcuts import render
from contact.models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        order_id = request.POST.get('order-id')
        message = request.POST.get('message')

        # Create a new Contact instance and save it to the database
        contact = Contact(name=name, email=email, subject=subject, order_id=order_id, message=message)
        contact.save()

        # Optionally, you can add a success message or redirect
        return render(request, 'contact/contact.html', {'success': 'Your message has been sent successfully!'})

    return render(request, 'contact/contact.html')
