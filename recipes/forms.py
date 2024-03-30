from django import forms

from .models import Recipes


class RecipesModelForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('title',
                  'description',
                  'cooking_steps',
                  'image',
                  'status')
