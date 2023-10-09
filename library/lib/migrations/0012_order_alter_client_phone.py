# Generated by Django 4.1.6 on 2023-06-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0011_client_provider_delete_basket_mat_provider'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва:')),
                ('price', models.CharField(default='0', max_length=50, verbose_name='Ціна:')),
                ('kilo', models.IntegerField(default=0, verbose_name='Кількість')),
                ('allprice', models.CharField(default='6 500грн', max_length=50, verbose_name='Разом:')),
                ('name', models.CharField(max_length=50, verbose_name="Ім'я:")),
                ('phone', models.CharField(default='', max_length=50, verbose_name='Номер телефону:')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default='', max_length=50, verbose_name='Кількість:'),
        ),
    ]
