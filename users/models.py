from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = PhoneNumberField(blank=True, verbose_name='Телефон', help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, verbose_name='Аватар', null=True, help_text='Загрузите изображение')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Страна', help_text='Введите название страны')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
