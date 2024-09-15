from django.contrib import admin
from .models import contact

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

admin.site.register(contact, contactAdmin)
