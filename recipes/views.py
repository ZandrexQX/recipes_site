from django.shortcuts import render
from .models import Recipes

def index(request):
    recipes = Recipes.objects.all()
    return render(request, 'index.html', {'recipes': recipes})
