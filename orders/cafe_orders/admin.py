from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'total_price', 'status')
    list_filter = ('status',)
    search_fields = ('table_number',)
    ordering = ('-id',)


admin.site.register(Order, OrderAdmin)
