from django.contrib import admin

from .models import *


class MatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(MAT, MatAdmin)
admin.site.register(provider)
admin.site.register(client)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in order._meta.fields]

    class Meta:
        model = order

admin.site.register(order, OrderAdmin)
