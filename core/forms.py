from django import forms
from .models import Subscriber, Contact

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your mail'}),
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get('email')
    #     if email:
    #         if Subscriber.objects.filter(email=email).exists():
    #             raise forms.ValidationError('Email already exists')
    #         return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('gmail.com'):
            raise forms.ValidationError('Invalid email address')
        elif Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name_and_surname', 'email_address', 'text')
        widgets = {
            'name_and_surname': forms.TextInput(attrs={'class': 'form-control' 'col-lg-6 col-md-6', 'placeholder': 'Your name and surname'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control' 'col-lg-6 col-md-6', 'placeholder': 'Your email'}),
            'text': forms.Textarea(attrs={'class': 'form-control' 'text-center', 'placeholder': 'Your message'}),
        }