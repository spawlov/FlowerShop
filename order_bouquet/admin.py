from django.contrib import admin
from .models import Category, Bouquet, Client, Order, Consultation

admin.site.register(Category)
admin.site.register(Bouquet)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Consultation)

