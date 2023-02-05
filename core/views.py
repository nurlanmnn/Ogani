from django.shortcuts import render

from core.forms import SubscriberForm, ContactForm
from .models import Setting, Contact

# Create your views here.


def contact(request):
    contact = Contact.objects.first()
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
    context = {
        'contact': contact,
        'contact_form': contact_form
    }
    return render(request, 'contact.html', context)

def index(request):
    setting = Setting.objects.first()
    subscribe_form = SubscriberForm()
    if request.method == 'POST':
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            subscribe_form = SubscriberForm()

    context = {
        'settings': setting,
        'subscribe_form': subscribe_form,
    }
    return render(request, 'index.html', context)



def checkout(request):
    context = {
        'checkout': checkout
    }
    return render(request, 'checkout.html', context)

def aboutus(request):
    context = {
        'aboutus': aboutus
    }
    return render(request, 'aboutus.html', context)

