from django.contrib import admin

from order.models import *

# Register your models here.


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['product_version_id']
    list_filter = ['product_version_id']


# class UserAdmin(admin.ModelAdmin):
#     list_display = ['name', 'lastname', 'phone']
#     list_filter = ['name', 'lastname', 'phone']


admin.site.register(Wishlists,WishlistAdmin)
admin.site.register(Cart)
admin.site.register(Cart_items)
# admin.site.register(User,UserAdmin)
