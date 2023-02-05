from django.shortcuts import render, HttpResponseRedirect, redirect
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
    context = {
        'settings': setting,
    }
    return render(request, 'index.html', context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # save the form data to database
            form.save()
            # redirect the user to a success page
            return redirect('index')
    else:
        form = SubscriberForm()
    return render(request, '_footer.html', {'subscribe_form': form})


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

