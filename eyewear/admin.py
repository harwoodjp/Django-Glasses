from django.contrib import admin

from .models import item

# Register your models here.

class itemAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price']


admin.site.register(item, itemAdmin)
