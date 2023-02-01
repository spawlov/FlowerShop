from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    title = models.CharField(max_length=255)


class Bouquet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )
    in_stock = models.BooleanField(default=False)
    number_of_sold = models.IntegerField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='bouquets')

    class Meta:
        verbose_name = 'букет'
        verbose_name_plural = 'букеты'

    def __str__(self):
        return f'Bouquet {self.name}'


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f'Client - {self.name}'


class Order(models.Model):
    order_statuses = (
        ('ACCEPTED', 'Принят'),
        ('PROCESSING', 'Обрабатывается'),
        ('BEING_DELIVERED', 'Доставляется'),
        ('CANCELLED', 'Отменен'),
        ('DELIVERED', 'Доставлен')
    )

    delivery_times = (
        ('AS_SOON_AS_POSSIBLE', 'Как можно скорее'),
        ('FROM_10_TO_12', 'с 10:00 до 12:00'),
        ('FROM_12_TO_14', 'с 12:00 до 14:00'),
        ('FROM_14_TO_16', 'с 14:00 до 16:00'),
        ('FROM_16_TO_18', 'с 16:00 до 18:00'),
        ('FROM_18_TO_20', 'с 18:00 до 20:00'),
    )

    bouquet = models.ForeignKey(Bouquet, on_delete=models.PROTECT, related_name='bouquet_orders')
    manager = models.ForeignKey(User, on_delete=models.PROTECT, related_name='manager_orders')
    courier = models.ForeignKey(User, on_delete=models.PROTECT, related_name='courier_orders')
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='client_orders')
    address = models.CharField(max_length=255)
    status = models.CharField(choices=order_statuses, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivery_time = models.CharField(choices=delivery_times, max_length=19)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Order - {self.bouquet.name}(bouquet) {self.client.name}(client)'


class Consultation(models.Model):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField()

    class Meta:
        verbose_name = 'консультация'
        verbose_name_plural = 'консультации'

    def __str__(self):
        return f'Consultation {self.name}'
