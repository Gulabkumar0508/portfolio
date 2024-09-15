from django.shortcuts import render
from .models import contact

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact = contact(name=name, email=email, phone=phone, message=message)
        Contact.save()
        return render(request, 'home.html', {'success_message': 'Your message has been sent successfully!'})
    return render(request, 'home.html')