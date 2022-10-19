from django.contrib import admin
from modeltranslation.admin import TranslationAdmin 
from product.models import *

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['created_at','product_image','updated_at']
    list_filter = ['created_at']

class CategoryAdmin(TranslationAdmin):
    pass
   
    
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product_version)
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Color)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Image,ImageAdmin)
