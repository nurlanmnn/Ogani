from core.models import Setting
from core.forms import SubscriberForm


def header(request):
    setting = Setting.objects.first()
    context = {
        'settings' : setting,
    }
    return context


def subscribe_form(request):
    return {'subscribe_form': SubscriberForm()}
