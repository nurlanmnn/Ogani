from django.contrib import admin
from .models import MyUser
# Register your models here.

# admin.site.register(MyUser)

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'bio', 'password')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')