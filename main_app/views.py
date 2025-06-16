from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

# Create your views here.

# Home and About Views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Recipe Views

@login_required
def recipe_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    ingredient_form = IngredientForm()
    return render(request, 'recipes/details.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'ingredient_form': ingredient_form,
    })

@login_required
def add_ingredient(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
    return redirect('recipe-detail', recipe_id=recipe_id)

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'recipe_id': self.object.pk})

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    pk_url_kwarg = 'recipe_id'

    def test_func(self):
        recipe = self.get_object()
        return recipe.user == self.request.user

    def get_success_url(self):
        return reverse('recipe-detail', kwargs={'recipe_id': self.object.pk})

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    pk_url_kwarg = 'recipe_id'

    def test_func(self):
        recipe = self.get_object()
        return recipe.user == self.request.user

    def get_success_url(self):
        return reverse('recipe-index')

# Ingredient Views

@login_required
def ingredient_list(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    return render(request, 'ingredients/ingredient_list.html', {'recipe': recipe, 'ingredients': ingredients})

@login_required
def ingredient_create(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('ingredient-list', recipe_id=recipe_id)
    else:
        form = IngredientForm()
    return render(request, 'ingredients/ingredient_form.html', {'form': form, 'recipe': recipe})

@login_required
def ingredient_update(request, recipe_id, ingredient_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredient = Ingredient.objects.get(id=ingredient_id, recipe=recipe)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient-list', recipe_id=recipe_id)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredients/ingredient_form.html', {'form': form, 'recipe': recipe})

@login_required
def ingredient_delete(request, recipe_id, ingredient_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredient = Ingredient.objects.get(id=ingredient_id, recipe=recipe)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list', recipe_id=recipe_id)
    return render(request, 'ingredients/ingredient_confirm_delete.html', {'ingredient': ingredient, 'recipe': recipe})