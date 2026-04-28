from django.conf import settings
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта', blank=True, null=True)
    image = models.ImageField(upload_to='catalog/photo', blank=True, null=True, verbose_name='изображение')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='products', verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за покупку')  # Исправлено
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')  # Исправлено
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')  # Исправлено
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='products',
    verbose_name="Владелец",
    null=True,
    blank=True,
)

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
        verbose_name = 'Категория'  # Исправлено
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name