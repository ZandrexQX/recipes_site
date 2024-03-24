from django.contrib import admin
from .models import Recipes

@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status']
    ordering = ['author', '-status']
    list_filter = ['date_add']
    search_fields = ['title', 'author']
    search_help_text = 'Поиск по полю "Наименование"'

    fields = ['date_add', 'title', 'description', 'cooking_steps', 'status', 'image', 'author']
    readonly_fields = ['date_add']
