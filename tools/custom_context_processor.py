# from django.http import HttpResponse, HttpRequest
# from django.forms import ModelForm
# from django import forms
# from Ogani.core.forms import SubscriberForm
# from core.models import Subscriber

# class SubscriberForm(forms.ModelForm):
#     class Meta:
#         model = Subscriber
#         fields = ['email',]
#         widgets = {
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter your mail'}),
#         }
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('gmail.com'):
    #         raise forms.ValidationError('Invalid email address')
    #     elif Subscriber.objects.filter(email=email).exists():
    #         raise forms.ValidationError('Email already exists')
    #     return email


# def subscribe_view(request: HttpRequest) -> HttpResponse:
#     subscribe_form = SubscriberForm()
#     if request.method == 'POST':
#         subscribe_form = SubscriberForm(request.POST)
#         if subscribe_form.is_valid():
#             subscribe_form.save()
#             subscribe_form = SubscriberForm()
    
#     return {
#         'subscribe_form': subscribe_form,
#     }