from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Bouquet, Client, Order, Consultation


class OrderInline(admin.TabularInline):
    model = Order

    fields = (
        'courier',
        'client',
        'address',
        'status',
        'delivery_time'
    )
    ordering = ('updated_at', )


class BouquetAdmin(admin.ModelAdmin):
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="200px" height="200px">')

    readonly_fields = ('preview', )

    inlines = (
        OrderInline,
    )


admin.site.register(Category)
admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Consultation)

