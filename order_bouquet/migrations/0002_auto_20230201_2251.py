# Generated by Django 3.2.16 on 2023-02-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_bouquet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AddField(
            model_name='bouquet',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='image',
            field=models.ImageField(default=10, upload_to='images/catalog'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bouquet',
            name='structure',
            field=models.CharField(default=10, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bouquet',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]