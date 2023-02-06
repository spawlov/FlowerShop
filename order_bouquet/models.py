from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'


class Bouquet(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    structure = models.CharField(
        max_length=255,
        verbose_name='Состав',
    )
    price = models.IntegerField(
        verbose_name='Цена',
    )
    in_stock = models.BooleanField(
        default=False,
        verbose_name='В наличии',
    )
    number_of_sold = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Кол-во проданных',
    )
    category = models.ManyToManyField(
        Category,
        related_name='bouquets',
        verbose_name='Категория',
    )
    image = models.ImageField(
        upload_to='images/catalog',
        verbose_name='Изображение',
    )
    width = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Ширина',
    )
    height = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Высота',
    )

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )
    phone = PhoneNumberField(
        verbose_name='Телефон',
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Эл. почта',
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    order_statuses = (
        ('NOT_PAID', 'Не оплачен'),
        ('ACCEPTED', 'Принят'),
        ('PROCESSING', 'Обрабатывается'),
        ('BEING_DELIVERED', 'Доставляется'),
        ('CANCELLED', 'Отменен'),
        ('DELIVERED', 'Доставлен'),
    )

    delivery_times = (
        ('AS_SOON_AS_POSSIBLE', 'Как можно скорее'),
        ('FROM_10_TO_12', 'с 10:00 до 12:00'),
        ('FROM_12_TO_14', 'с 12:00 до 14:00'),
        ('FROM_14_TO_16', 'с 14:00 до 16:00'),
        ('FROM_16_TO_18', 'с 16:00 до 18:00'),
        ('FROM_18_TO_20', 'с 18:00 до 20:00'),
    )

    bouquet = models.ForeignKey(
        Bouquet,
        on_delete=models.PROTECT,
        related_name='bouquet_orders',
        verbose_name='Букет',
    )
    manager = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='manager_orders',
        verbose_name='Менеджер',
    )
    courier = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='courier_orders',
        verbose_name='Курьер',
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name='client_orders',
        verbose_name='Заказчик',
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес доставки',
    )
    status = models.CharField(
        choices=order_statuses,
        max_length=15,
        verbose_name='Статус',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Обновлен',
    )
    delivery_time = models.CharField(
        choices=delivery_times,
        max_length=19,
        verbose_name='Время доставки',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order - {self.bouquet.name} {self.client.name}'


class Consultation(models.Model):
    status = (
        ('WAITING', 'Ожидание'),
        ('COMPLETED', 'Проведена'),
    )
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = PhoneNumberField(verbose_name='Телефон')
    status = models.CharField(
        max_length=9,
        choices=status,
        default='WAITING',
        verbose_name='Статус',
    )

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

    def __str__(self):
        return f'{self.name}'
