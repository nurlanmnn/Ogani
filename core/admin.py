from django.contrib import admin

from .models import (
    Advertisement, FeaturedProduct, LatestProduct, Subscriber, Setting, AboutUs, 
    SecureShopping, PrivacyPolicy, 
    Contact, Image
    )

# Register your models here.
admin.site.register(Subscriber)

admin.site.register(SecureShopping)
admin.site.register(PrivacyPolicy)
admin.site.register(Image)
admin.site.register(Advertisement)
admin.site.register(FeaturedProduct)
admin.site.register(LatestProduct)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_and_surname', 'email_address', 'is_check')
    list_filter = ('is_check',)
    search_fields = ('name_and_surname',)
    # readonly_fields = ('email','text')


    fieldsets = (
        ('Personal info', {
            'fields': ('name_and_surname', 'email_address'),
            'classes': ('collapse'),
            'description': ('Burada ad, soyad ve email unvani verilmishdir.')
        }),
        ('Additional info', {
            'fields': ('text', 'is_check')
        }),
    )


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    inlines = [ImageInline,]