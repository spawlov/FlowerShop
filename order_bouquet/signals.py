from django.conf import settings
from django.core import mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Order, Consultation


def sending_mail(sender, recipients, subject, message_html):
    try:
        connection = mail.get_connection()
        connection.open()
    except Exception as e:
        return e
    else:
        for recipient in recipients:
            message = mail.EmailMultiAlternatives(
                subject=subject,
                from_email=sender,
                to=[recipient],
                connection=connection,
            )
            message.attach_alternative(message_html, 'text/html')
            message.send()
    return


@receiver(post_save, sender=Order)
def add_order(sender, instance, created, *args, **kwargs):
    if created:
        url = f'{settings.ALLOWED_HOSTS[0]}oder-edit/{instance.pk}/'
        html_content = render_to_string(
            'email/added_order.html',
            {
                'url': url,
            }
        )
        subject = f'Новый заказ №{instance.pk}'

        sending_mail(
            settings.EMAIL,
            settings.EMAIL_RECIPIENTS,
            subject,
            html_content
        )

    return


@receiver(post_save, sender=Consultation)
def add_order(sender, instance, created, *args, **kwargs):
    if created:
        url = f'{settings.ALLOWED_HOSTS[0]}consultation-edit/{instance.pk}/'
        html_content = render_to_string(
            'email/added_consultation.html',
            {
                'url': url
            }
        )
        subject = 'Новый запрос консультации'

        sending_mail(
            settings.EMAIL,
            settings.EMAIL_RECIPIENTS,
            subject,
            html_content
        )

    return
