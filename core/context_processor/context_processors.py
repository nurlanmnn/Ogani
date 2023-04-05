from shop.models import CartItem
from shop.views import _cart_id
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

from shop.models import Cart

def cart_context(request, total_quantity=0):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total_quantity += cart_item.quantity
            # total_quantity += cart_item.quantity
    except ObjectNotExist:
        pass
    return {'total_quantity': total_quantity}
