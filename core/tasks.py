from celery import shared_task
from core.models import Subscriber
from django.core.mail import EmailMultiAlternatives
from django.conf import settings 
from core.views import settings as sety

# test simple task repeat every 10 seconds with crontab

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.all().values_list('email',flat=True)
    mail_text = f"Hi, <br> This email is sent from Ogani company <br> Thanks for your patience <br> <h1> Site commitee </h1>"

    msg = EmailMultiAlternatives(subject='Test subject', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()


send_mail_to_subscribers.delay()
# (is_active=True) bu unsub
