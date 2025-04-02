from django.contrib import admin

from .models import Order, OrderDish


class OrderDishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', )
    list_filter = ('name',)
    search_fields = ('name',)


class OrderDishInline(admin.TabularInline):
    model = OrderDish


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'total_price', 'status')
    list_filter = ('status',)
    search_fields = ('table_number',)
    ordering = ('-id',)
    inlines = [OrderDishInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDish, OrderDishAdmin)
