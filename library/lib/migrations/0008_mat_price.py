# Generated by Django 4.1.6 on 2023-06-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0007_mat_delete_books_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='mat',
            name='price',
            field=models.CharField(default='0', max_length=50, verbose_name='Ціна:'),
        ),
    ]
