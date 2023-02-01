from django.urls import path

from order_bouquet.views import index


urlpatterns = [
    path('', index, name='home'),
]
