from django.shortcuts import render

# Create your views here.
def shop(request):
    shop = shop.objects.all()
    context = {
        'shop': shop
    }
    return render(request, 'shop-details.html', context)