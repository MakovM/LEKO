# Generated by Django 4.1.6 on 2023-06-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0017_order_all_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Номер телефону:'),
        ),
    ]
