from django.contrib import admin
from .models import Recipe, Ingredient

# Register your Models

admin.site.register(Recipe)

# Register Ingredients
admin.site.register(Ingredient)