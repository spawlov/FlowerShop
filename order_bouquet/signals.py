from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Order, Consultation


@receiver(post_save, sender=Order)
def add_order(sender, instance, created, *args, **kwargs):
    if created:
        html_content = render_to_string(
            'email/added_order.html',
            {

            }
        )
        subject = f'Новый заказ №{instance.pk}'
        send_mail(
            subject, html_content, settings.EMAIL, settings.EMAIL_RECIPIENTS
        )
    return


@receiver(post_save, sender=Consultation)
def add_order(sender, instance, created, *args, **kwargs):
    if created:
        html_content = render_to_string(
            'email/added_consultation.html',
            {

            }
        )
        subject = f'Новый запрос консультации'
        send_mail(
            subject, html_content, settings.EMAIL, settings.EMAIL_RECIPIENTS
        )
    return
