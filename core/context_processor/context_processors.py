from core.models import Setting

def header(request):
    setting = Setting.objects.first()
    context = {
        'settings' : setting,
    }
    return context