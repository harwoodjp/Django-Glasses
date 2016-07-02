from django.contrib import admin

from .models import Item, Cart2, CartItem, Glasses

# Register your models here.

admin.site.site_url = "/eyewear/"

class glassesAdmin(admin.ModelAdmin):
    fields = ['frame_name']


class itemAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price']

class cartAdmin(admin.ModelAdmin):
    fields = ['item']


class cart2Admin(admin.ModelAdmin):
    fields = ['owner','name']


class CartItemAdmin(admin.ModelAdmin):
    fields = ['cart','item']


admin.site.register(Item, itemAdmin)
admin.site.register(Cart2, cart2Admin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Glasses, glassesAdmin)


