from django.shortcuts import render
from forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
import backend as credential


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name.title(), last_name=last_name.title(), email=email, date=date,
                                occupation=occupation)

            # email to applicant
            message_body = f"A new job application was submitted. Thank you, {first_name.title()}"
            email_message = EmailMessage("Form submission conformation", message_body, to=[email])
            email_message.send()

            # email to host
            mes_body = f"{first_name} submitted an application with the details: \n" \
                       f"First Name:{first_name.title()}  \n Last Name:{last_name.title()} \n" \
                       f"Email:{email} \n Date:{date} \n Occupation:{occupation}"
            host_email = EmailMessage("Form Submission", mes_body, to=[credential.username()])
            host_email.send()

            messages.success(request, "Form submitted successfully!")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")