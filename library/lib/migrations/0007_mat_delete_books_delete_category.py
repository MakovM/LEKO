# Generated by Django 4.1.6 on 2023-06-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0006_alter_books_options_remove_books_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва:')),
                ('slug', models.SlugField(unique=True, verbose_name='Url:')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото:')),
                ('content', models.TextField(verbose_name='Опис:')),
                ('availability', models.CharField(choices=[('1', 'В наявності'), ('2', 'Немає в наявності')], default='', max_length=25, verbose_name='Наявність')),
                ('number', models.IntegerField(default=0, verbose_name='Кількість:')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товар',
            },
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
