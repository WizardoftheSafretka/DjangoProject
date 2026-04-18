from django.db import models

# Product: наименование, описание, изображение, категория, цена за покупку, дата создания, дата последнего изменения.

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта', blank=True, null=True)
    image = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='изображение')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(verbose_name='цена за покупку')
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
        permissions = [
            ('can_unpublish_product', 'Can unpublish product')
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование категории')
    description = models.TextField(verbose_name='описание категории', blank=True, null=True)

    class Meta:
        verbose_name = 'Категрия'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name
