from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Menu(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)  # Название меню
    slug = models.SlugField('Слаг', unique=True, db_index=True)  # Слаг меню
    parent = models.ForeignKey('Menu', on_delete=models.CASCADE, **NULLABLE,
                               related_name='children')  # Родительское меню
    created = models.DateTimeField('Дата создания', auto_now_add=True)  # Дата создания меню

    class Meta(object):
        ordering = ('-created',)  # Сортировка объектов по дате создания в обратном порядке
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return self.name
