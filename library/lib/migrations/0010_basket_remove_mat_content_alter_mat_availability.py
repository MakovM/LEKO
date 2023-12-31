# Generated by Django 4.1.6 on 2023-06-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0009_alter_mat_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва:')),
                ('slug', models.SlugField(unique=True, verbose_name='Url:')),
                ('price', models.CharField(max_length=50, verbose_name='Ціна:')),
                ('number', models.IntegerField(default=0, verbose_name='Кількість:')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
            },
        ),
        migrations.RemoveField(
            model_name='mat',
            name='content',
        ),
        migrations.AlterField(
            model_name='mat',
            name='availability',
            field=models.CharField(choices=[('В наявності', 'В наявності'), ('Немає в наявності', 'Немає в наявності')], max_length=25, verbose_name='Наявність'),
        ),
    ]
