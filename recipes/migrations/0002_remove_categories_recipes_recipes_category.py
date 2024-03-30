# Generated by Django 4.2.6 on 2024-03-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='recipes',
        ),
        migrations.AddField(
            model_name='recipes',
            name='category',
            field=models.ManyToManyField(default=None, to='recipes.categories', verbose_name='Категории'),
        ),
    ]
