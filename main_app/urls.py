from django.urls import path
from . import views

urlpatterns = [
    # Home and About
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Recipe URLs
    path('recipes/', views.recipe_index, name='recipe-index'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/<int:recipe_id>/edit/', views.RecipeUpdateView.as_view(), name='recipe-edit'),
    path('recipes/<int:recipe_id>/delete/', views.RecipeDeleteView.as_view(), name='recipe-delete'),

    # Ingredient URLs
    path('recipes/<int:recipe_id>/ingredients/', views.ingredient_list, name='ingredient-list'),
    path('recipes/<int:recipe_id>/ingredients/add/', views.ingredient_create, name='ingredient-create'),
    path('recipes/<int:recipe_id>/ingredients/<int:ingredient_id>/edit/', views.ingredient_update, name='ingredient-edit'),
    path('recipes/<int:recipe_id>/ingredients/<int:ingredient_id>/delete/', views.ingredient_delete, name='ingredient-delete'),

    # Optional: Add ingredient directly from recipe detail page (via POST)
    path('recipes/<int:recipe_id>/ingredients/add-direct/', views.add_ingredient, name='add-ingredient-direct'),
]
