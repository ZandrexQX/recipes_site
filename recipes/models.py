from django.db import models
from django.contrib.auth.models import User

class Recipes(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Categories(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')
    recipes = models.ManyToManyField(Recipes, verbose_name='Рецепты')

    def __str__(self):
        return self.title
