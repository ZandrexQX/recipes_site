from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/add', views.recipe_form, name='recipe_form'),
]
