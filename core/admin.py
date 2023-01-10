from django.contrib import admin

from .models import Student, Subscriber, Setting, AboutUs, AboutOurShop, SecureShopping, PrivacyPolicy, WhoWeAre, Contact

# Register your models here.

admin.site.register(Student)
admin.site.register(Subscriber)
admin.site.register(Setting)
admin.site.register(AboutUs)
admin.site.register(AboutOurShop)
admin.site.register(SecureShopping)
admin.site.register(PrivacyPolicy)
admin.site.register(WhoWeAre)
admin.site.register(Contact)