from django.contrib import admin
from .models import *
# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ['countries']
    list_filter = ['countries']


class StateAdmin(admin.ModelAdmin):
    list_display = ['state']
    list_filter = ['state']


class CityAdmin(admin.ModelAdmin):
    list_display = ['city']
    list_filter = ['city']
    
admin.site.register(User)
admin.site.register(Billing)
admin.site.register(Different_shipping)
admin.site.register(Newsletter)
