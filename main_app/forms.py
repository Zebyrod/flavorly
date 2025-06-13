from django import forms
from .models import Recipe, Ingredient
from django.forms.models import inlineformset_factory


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'recipe_type', 'instructions']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['amount', 'unit', 'name']

IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,  # Use your custom IngredientForm
    fields=['amount', 'unit', 'name'],
    extra=1,  # How many blank ingredient forms you want initially
    can_delete=True  # Allow deleting ingredients
)