from django.contrib import admin
from .models import   *


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']
    list_filter = ['name','email']
    

admin.site.register(Contact,ContactAdmin)
