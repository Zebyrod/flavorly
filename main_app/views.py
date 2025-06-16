from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

# Home and About Views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# Recipe Views Function based views 

@login_required
def recipe_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
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
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, f"Recipe '{recipe.name}' created successfully!")
            return redirect('recipe-detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_update(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.user != request.user:
        return redirect('recipe-index')  # simple permission check

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, f"Recipe '{recipe.name}' updated successfully!")
            return redirect('recipe-detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form, 'recipe': recipe})

@login_required
def recipe_delete(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if recipe.user != request.user:
        return redirect('recipe-index')

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, f"Recipe '{recipe.name}' deleted successfully.")
        return redirect('recipe-index')

    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


# Ingredient Views function based views 

@login_required
def ingredient_list(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe=recipe)
    return render(request, 'ingredients/ingredient_list.html', {
        'recipe': recipe,
        'ingredients': ingredients
    })

@login_required
def ingredient_create(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            messages.success(request, f"Ingredient '{ingredient.name}' added to '{recipe.name}'.")
            return redirect('ingredient-list', recipe_id=recipe.id)
    else:
        form = IngredientForm()
    return render(request, 'ingredients/ingredient_form.html', {
        'form': form,
        'recipe': recipe
    })

@login_required
def ingredient_delete(request, recipe_id, ingredient_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredient = Ingredient.objects.get(id=ingredient_id, recipe=recipe)

    if request.method == 'POST':
        ingredient.delete()
        messages.success(request, f"Ingredient '{ingredient.name}' deleted from '{recipe.name}'.")
        return redirect('ingredient-list', recipe_id=recipe.id)

    return render(request, 'ingredients/ingredient_confirm_delete.html', {
        'ingredient': ingredient,
        'recipe': recipe
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after signup
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})