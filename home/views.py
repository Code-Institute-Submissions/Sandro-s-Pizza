from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from product.models import Item


def index(request):
    """Renders index page"""
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home/index.html', context)


def contact(request):
    """Renders contact page and send the message via email"""
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
    """Renders message sent page"""
    return render(request, "home/message_sent.html")


def handler_500(request):
    """Handles 500 error"""
    return render(request, "home/404.html")


def handler_404(request, exception):
    """Handles 404 error"""
    return render(request, "home/404.html")
