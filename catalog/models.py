from django.db import models

# Product: наименование, описание, изображение, категория, цена за покупку, дата создания, дата последнего изменения.

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='home/photo', blank=True, null=True, verbose_name='изображение')
    category =
    price = models.FloatField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(verbose_name='дата создания')
    updated_at = models.DateTimeField(verbose_name='дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = 'name'

