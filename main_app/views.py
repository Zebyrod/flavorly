from django.shortcuts import render, redirect 
from .models import Recipe, Ingredient
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .forms import RecipeForm, IngredientFormSet, IngredientForm
from django.forms import formset_factory

# Create your views here.

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def recipe_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    # Render the recipes/index.html with the data
    return render(request, 'recipes/index.html', {'recipes': recipes })

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe=recipe)

    # instantiate the ingredient form to be rendered in the recipe template
    IngredientFormSet = formset_factory(IngredientForm, extra=1)
    return render(request, 'recipes/details.html', {
        'recipe': recipe,
        'ingredients': ingredients 
    })

# Since I ended up using a formset I had to vastly refactor my views.py file from what was used in class to achieve the functionality I wanted. The goal was to have a separate model for ingredients and allow the user to add as many ingredients as necessary for the recipe. Using formset required me to add alot to my class based views

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_formset'] = IngredientFormSet(self.request.POST, prefix='ingredients')
        else:
            context['ingredient_formset'] = IngredientFormSet(prefix='ingredients')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_formset = context['ingredient_formset']

        if ingredient_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()

            ingredients = ingredient_formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = self.object
                ingredient.save()

            # Handle any deleted ingredients
            for ingredient in ingredient_formset.deleted_objects:
                ingredient.delete()

            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'  # reuse the same template
    success_url = reverse_lazy('recipe-index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_formset'] = IngredientFormSet(self.request.POST, instance=self.object)
        else:
            context['ingredient_formset'] = IngredientFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_formset = context['ingredient_formset']

        if ingredient_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()

            ingredients = ingredient_formset.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = self.object
                ingredient.save()

            # Delete ingredients marked for deletion
            for ingredient in ingredient_formset.deleted_objects:
                ingredient.delete()

            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
