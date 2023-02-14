from django import forms
from .models import Subscriber, Contact
from django.utils.translation import gettext_lazy as _


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': _('Enter your mail')}),
        }

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('gmail.com'):
            raise forms.ValidationError(_('Invalid email address'))
        elif Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Email already exists'))
        return email


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name_and_surname', 'email_address', 'text')
        widgets = {
            'name_and_surname': forms.TextInput(attrs={'class': 'form-control' 'col-lg-6 col-md-6', 'placeholder': _('Your name and surname')}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control' 'col-lg-6 col-md-6', 'placeholder': _('Your email')}),
            'text': forms.Textarea(attrs={'class': 'form-control' 'text-center', 'placeholder': _('Your message')}),
        }