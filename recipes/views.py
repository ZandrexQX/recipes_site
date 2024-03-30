import logging

from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Recipes
from .forms import RecipesModelForm



logger = logging.getLogger(__name__)

def index(request):
    recipes = Recipes.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe_form(request):
    if request.method == 'POST':
        form = RecipesModelForm(request.POST, request.FILES)
        message = 'Ошибка данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cooking_steps = form.cleaned_data['cooking_steps']
            image = form.cleaned_data['image']
            author = request.user
            status = form.cleaned_data['status']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            recipe = Recipes(title=title, description=description, cooking_steps=cooking_steps,
                              author=author, image=image, status=status)
            recipe.save()
            logger.info(f"Product {recipe.title} created")
            message = f'Рецепт {recipe.title} сохранен'
    else:
        form = RecipesModelForm()
        message = 'Заполните форму'
    return render(request, 'recipe_form.html', {'form': form, 'message': message})
