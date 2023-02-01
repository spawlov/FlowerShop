from django.urls import path


from flower_shop.views import index

urlpatterns = [
    path('', index, name='mainpage'),
]
