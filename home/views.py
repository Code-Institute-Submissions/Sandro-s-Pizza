from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(
                    subject, message, body['email'],
                    ['sandro.bencinic@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("message_sent")
        form = ContactForm()
    return render(request, "home/contact.html", {'form': form})


def message_sent(request):
    return render(request, "home/message_sent.html")
