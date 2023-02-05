from core.models import Setting, Subscriber
# from core.views import subscribe_view

def header(request):
    setting = Setting.objects.first()
    context = {
        'settings' : setting,
    }
    return context

# def subscribe_processor(request):
#     # Get the subscribe_view data
#     subscribe_view = subscribe_view.objects.all()
#     # Return a dictionary with the subscribe_view data
#     return {'subscribe_view': subscribe_view}

# def subscribe(request):
#     subscribe_form = SubscriberForm()
#     if request.method == 'POST':
#         subscribe_form = SubscriberForm(request.POST)
#         if subscribe_form.is_valid():
#             subscribe_form.save()
#             subscribe_form = SubscriberForm()

#     context = {
#         'subscribe_form': subscribe_form,
#     }
#     return context