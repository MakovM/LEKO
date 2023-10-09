from django.db import models
from django.urls import reverse


availability = (
    ('В наявності', 'В наявності'),
    ('Немає в наявності', 'Немає в наявності')
)
class provider(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва:')
    product = models.CharField(max_length=50, verbose_name='Продукт:')
    price = models.CharField(max_length=50, verbose_name='Ціна:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Постачальник'
        verbose_name_plural = 'Постачальники'


class MAT(models.Model):
    title = models.CharField(max_length=50, verbose_name='Назва:')
    slug = models.SlugField(max_length=50, verbose_name='Url:', unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото:')
    price = models.CharField(max_length=50, verbose_name='Ціна:', default='6 500грн')
    availability = models.CharField(max_length=25, verbose_name='Наявність', choices=availability)
    number = models.IntegerField(default=0, verbose_name='Кількість:')
    provider = models.ManyToManyField(provider, related_name='providers', verbose_name='Постачальник:')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'



    def get_absolute_url(self):

        return reverse('mat', kwargs={"slug": self.slug})


class order(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50, verbose_name='Назва:')
    price = models.CharField(null=True, blank=True, max_length=50, verbose_name='Ціна:', default='0')
    kilo = models.IntegerField(null=True, blank=True, verbose_name='Кількість')
    all_price = models.CharField(null=True, blank=True, max_length=50, verbose_name='Разом:', default='0')
    name = models.CharField(null=True, blank=True, max_length=50, verbose_name="Ім'я:")
    phone = models.CharField(null=True, blank=True, max_length=50, verbose_name='Номер телефону:', default='0')


    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Назва:')
    phone = models.CharField(max_length=50, default='', verbose_name='Кількість:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'