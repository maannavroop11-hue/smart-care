from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "general").strip()
        message_text = request.POST.get("message", "").strip()
        consent = request.POST.get("consent") == "on"

        valid_subjects = {
            choice[0]
            for choice in ContactMessage.SUBJECT_CHOICES
        }

        if not all([name, email, message_text]):
            messages.error(
                request,
                "Please complete your name, email and message."
            )

        elif len(name) > 100 or len(email) > 254 or len(phone) > 20:
            messages.error(
                request,
                "Please check the length of your contact details."
            )

        elif subject not in valid_subjects:
            messages.error(
                request,
                "Please choose a valid subject."
            )

        elif not consent:
            messages.error(
                request,
                "Please confirm that you agree to be contacted."
            )

        else:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message_text,
            )

            messages.success(
                request,
                "Thank you! Your message has been submitted successfully."
            )

            return redirect("contact")

    return render(request, "contact.html")
