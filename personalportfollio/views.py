from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from django.conf import settings

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the message to database
        Contact.objects.create(name=name, email=email, message=message)

        # Send email
        send_mail(
            subject=f"New Contact from {name}",
            message=f"Email: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
            fail_silently=False,
        )

        messages.success(request, "Thank you for contacting me! I’ll get back to you soon.")
        return redirect('index')  # or 'index' depending on your URL name

    return render(request, "index.html")
