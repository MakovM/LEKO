# Generated by Django 4.1.6 on 2023-06-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0015_alter_order_kilo_alter_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name="Ім'я:"),
        ),
        migrations.AlterField(
            model_name='order',
            name='kilo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Кількість'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.CharField(blank=True, default='0', max_length=50, null=True, verbose_name='Ціна:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Назва:'),
        ),
    ]
