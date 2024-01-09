from django.shortcuts import render
from .forms import ApplicationForm, ContactForm
from .models import Form, ContactForm as CForm
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date,
                                occupation=occupation)

            message_body = (f"Thank you for your submission, {first_name}."
                            f"Here are your data: \n{first_name}\n{last_name}\n{date}\n{occupation}\n\n"
                            f"Thank you!")
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully")
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            CForm.objects.create(name=name, email=email, subject=subject,
                                       message=message)

            message_body = f"Thank you for your submission, {name}, about: {subject}."
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully")
    return render(request, "contact.html")
