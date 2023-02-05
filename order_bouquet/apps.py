from django.apps import AppConfig


class OrderBouquetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_bouquet'

    def ready(self):
        from . import signals
