from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое', blank=True, null=True)
    image = models.ImageField(upload_to='blogs/photo', blank=True, null=True, verbose_name='первью')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=0, verbose_name='Опубликовано')
    count_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров", editable=False)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('title',)

    def __str__(self):
        return self.title
