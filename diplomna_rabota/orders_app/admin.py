from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1  # one empty row for adding new entries
    fields = ('product', 'quantity')
    min_num = 1
    can_delete = True
    autocomplete_fields = ['product']  # Optional if product list is large

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'order_date', 'order_address', 'order_price',
        'payment_method', 'order_status', 'display_products',
        'client', 'employee', 'shipper'
    )
    list_display_links = ('id',)
    search_fields = ('id', 'client__username', 'employee__username', 'shipper__username')
    ordering = ('order_date',)
    inlines = [OrderProductInline]

    def display_products(self, obj):
        return ", ".join([
            f"{op.product.name} (x{op.quantity})"
            for op in obj.orderproduct_set.all()
        ])
    display_products.short_description = 'Products'

admin.site.register(Order, OrderAdmin)
