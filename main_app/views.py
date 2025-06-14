from django.shortcuts import render, redirect 
from .models import Recipe, Ingredient
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

# I refactored this code again to include a new MixIn, This mixin handles the formset logic. Instead of having this code repeated in all of my classes. I managed to move it all into a mixin and now I call that mixin in my other views to use the logic


class RecipeFormWithIngredientsMixin:
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['ingredient_formset'] = IngredientFormSet(self.request.POST, instance=getattr(self, 'object', None), prefix='ingredients')
        else:
            context['ingredient_formset'] = IngredientFormSet(instance=getattr(self, 'object', None), prefix='ingredients')
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

            for ingredient in ingredient_formset.deleted_objects:
                ingredient.delete()

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('recipe-detail', kwargs={'recipe_id': self.object.pk})


class RecipeCreate(LoginRequiredMixin, RecipeFormWithIngredientsMixin, CreateView):
    model = Recipe

class RecipeUpdate(LoginRequiredMixin, RecipeFormWithIngredientsMixin, UpdateView):
    model = Recipe

class RecipeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    # After they delete I want the user to be sent to the index page to see the recipe is now deleted.
    # I added in the UserPassesTestMixin to safeguard for the future implementation of a community page. 
    success_url = reverse_lazy('recipe-index')

    def test_func(self):
        # Ensure that only the owner can delete the recipe
        recipe = self.get_object()
        return recipe.user == self.request.user