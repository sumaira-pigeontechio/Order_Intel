from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request, "base.html")

def send_mail_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
        New Contact Message

        Name: {name}
        Email: {email}
        Subject: {subject}
        
        Message:
        {message}
        """

        send_mail(
            subject,
            full_message,
            email,  # from email
            ['yourgmail@gmail.com'],  # to email
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")

    return redirect("home")
