from django.contrib import admin

from .models import (
    Student, Subscriber, Setting, AboutUs, 
    AboutOurShop, SecureShopping, PrivacyPolicy, 
    WhoWeAre, Contact
    )

# Register your models here.

admin.site.register(Student)
admin.site.register(Subscriber)
admin.site.register(Setting)
admin.site.register(AboutUs)
admin.site.register(AboutOurShop)
admin.site.register(SecureShopping)
admin.site.register(PrivacyPolicy)
admin.site.register(WhoWeAre)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_and_surname', 'email_address')
    list_filter = ('is_check',)
    search_fields = ('name_and_surname',)
    # readonly_fields = ('email','text')

    fieldsets = (
            ('Personal info', {
                'fields': ('name_and_surname', 'email_address'),
                'classes': ('collapse'),
            }),
            ('Additional info', {
                'fields': ('text', 'is_check')
            }),
        )











