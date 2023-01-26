from django import forms
from .models import Subscriber

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