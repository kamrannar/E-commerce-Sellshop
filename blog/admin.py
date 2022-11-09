from django.contrib import admin
from .models import *
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author','text']
    list_filter = ['author','title','category']
    
    

admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(BlogStatistic)
admin.site.register(BlockedIP)