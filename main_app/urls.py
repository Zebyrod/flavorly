from django.urls import path, include
from . import views

urlpatterns = [
    # Home and About
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Recipe URLs
path('recipes/', views.recipe_index, name='recipe-index'),
path('recipes/create/', views.recipe_create, name='recipe-create'),
path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
path('recipes/<int:recipe_id>/edit/', views.recipe_update, name='recipe-edit'),
path('recipes/<int:recipe_id>/delete/', views.recipe_delete, name='recipe-delete'),

# Ingredient URLs
path('recipes/<int:recipe_id>/ingredients/', views.ingredient_list, name='ingredient-list'),
path('recipes/<int:recipe_id>/ingredients/add/', views.ingredient_create, name='ingredient-create'),
path('recipes/<int:recipe_id>/ingredients/<int:ingredient_id>/delete/', views.ingredient_delete, name='ingredient-delete'),

# Log In URLS
path('accounts/', include('django.contrib.auth.urls')),
path('accounts/signup/', views.signup, name='signup'),
]
