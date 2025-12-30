from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage, get_connection
from .forms import ContactForm
from django.conf import settings
import ssl


def home(request):
    form = ContactForm()
    return render(request, "home.html", {"form": form})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                # Import smtplib to patch SSL behavior
                import smtplib

                # Store original starttls method
                original_starttls = smtplib.SMTP.starttls

                # Create wrapper for starttls with disabled SSL verification
                def custom_starttls(self, **kwargs):
                    # Create SSL context that bypasses verification
                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    kwargs["context"] = context
                    return original_starttls(self, **kwargs)

                # Temporarily replace starttls method
                smtplib.SMTP.starttls = custom_starttls

                try:
                    # Send email using standard send_mail
                    send_mail(
                        subject="dtebar.pythonanywhere.com",
                        message=f"Name: {name}\nEmail: {email}\n\nMessage: {message}",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=["dtebar@gmail.com"],
                        fail_silently=False,
                    )
                    messages.success(request, "Your message has been sent.")
                finally:
                    # Restore original starttls method
                    smtplib.SMTP.starttls = original_starttls

            except Exception as e:
                messages.error(
                    request, f"An error occurred while sending your message: {e}"
                )

            return redirect("home")
    else:
        form = ContactForm()
    return render(request, "home.html", {"form": form})


def download_resume(request):
    file_path = "resumes/daniel-tebar-resume-2024.pdf"
    absolute_path = settings.BASE_DIR / "ts_v5_app/static" / file_path

    response = FileResponse(open(absolute_path, "rb"), content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="daniel-tebar-resume-2024.pdf"'
    )

    return response


def test_email(request):
    send_mail(
        "Hello from Daniel Tébar!",
        "Congratulations, your Django Mailgun email is working!",
        "postmaster@sandbox83c891ec455a4bbdb7f96031912fe08c.mailgun.org",  # From
        ["dtebar@gmail.com"],  # To
        fail_silently=False,
    )
    return HttpResponse("Email sent!")
