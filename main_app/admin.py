# from django.contrib import admin
# from .models import Recipe, Ingredient

# # Register your models here.
# admin.site.register(Recipe)
# admin.site.register(Ingredient)

from django.contrib import admin
from .models import Recipe, Ingredient

# Create an inline admin descriptor for Ingredient model
class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1  # Number of blank ingredient fields to display by default

# Register the Recipe model with Ingredient inlines
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

# Register only Recipe in the admin panel
admin.site.register(Recipe, RecipeAdmin)

# DO NOT register Ingredient on its own
# admin.site.register(Ingredient) ← remove or comment this out