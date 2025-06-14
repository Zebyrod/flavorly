from django import forms
from .models import Recipe, Ingredient
from django.forms.models import inlineformset_factory

# I went back in here and refactored my forms in order to implement the bootstrap styling without having to use a custom filter
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'recipe_type', 'instructions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'recipe_type': forms.Select(attrs={'class': 'form-select'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['amount', 'unit', 'name']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

IngredientFormSet = inlineformset_factory(
    Recipe,
    Ingredient,
    form=IngredientForm,
    fields=['amount', 'unit', 'name'],
    extra=1, # This will populate one blank form to start 
    can_delete=True # This quick line allows me to implement deletion of the ingredient within the form. This will be a checkbox where the user can click then save and it will delete. Will revisit this later to add in another view potentially where the user will get a are you sure page etc.  
)