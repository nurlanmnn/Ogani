from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from core.forms import SubscriberForm, ContactForm
from .models import FAQ, AboutUs, DeliveryInfo, PrivacyPolicy, SecureShopping, Setting, Contact, OurServices
from django.utils import translation
# from django.config import settings
from urllib.parse import urlparse
from django.contrib import messages

# Create your views here.


def contact(request):
    contact = Contact.objects.first()
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Successfully sent!')
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
    aboutus = AboutUs.objects.first()
    context = {
        'aboutus': aboutus
    }
    return render(request, 'aboutus.html', context)

def secureshopping(request):
    secureshopping = SecureShopping.objects.first()
    context = {
        'secureshopping': secureshopping
    }
    return render(request, 'secureshopping.html', context)

def ourservices(request):
    ourservices = OurServices.objects.first()
    context = {
        'ourservices': ourservices
    }
    return render(request, 'ourservices.html', context)

def privacypolicy(request):
    privacypolicy = PrivacyPolicy.objects.first()
    context = {
        'privacypolicy': privacypolicy
    }
    return render(request, 'privacypolicy.html', context)

def faq(request):
    faq = FAQ.objects.first()
    context = {
        'faq': faq
    }
    return render(request, 'faq.html', context)

def deliveryinfo(request):
    deliveryinfo = DeliveryInfo.objects.first()
    context = {
        'deliveryinfo': deliveryinfo
    }
    return render(request, 'deliveryinfo.html', context)


from django.utils import translation
from django.shortcuts import redirect
from django.conf import settings

def set_language(request):
    language = request.POST.get('language', settings.LANGUAGE_CODE)
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect('root')


# def set_language(request, language='en'):
#     for lang, _ in settings.LANGUAGES:
#         translation.activate(lang)
#     next_url = request.META.get("HTTP_REFERER")
#     if next_url:
#         translation.activate(language)
#         response = HttpResponseRedirect(next_url)
#         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
#     else:
#         response = HttpResponseRedirect("/")
#     return response

