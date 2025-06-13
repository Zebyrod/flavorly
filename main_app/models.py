from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    type_choices = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
        ('snack', 'Snack'),
        ('appetizer', 'Appetizer')
    ]
    recipe_type = models.CharField(max_length=20, choices=type_choices, default='breakfast')
    instructions = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name

class Ingredient(models.Model):
    unit_choices = [
        ('tsp', 'Teaspoon'),
        ('tbsp', 'Tablespoon'),
        ('cup', 'Cup'),
        ('oz', 'Ounce'),
        ('lb', 'Pound'),
        ('kg', 'Kilogram'),
        ('ml', 'Milliliter'),
        ('l', 'Liter'),
        ('unit', 'Whole')
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=10)
    unit = models.CharField(max_length=10, choices=unit_choices)

    def __str__(self):
        unit = self.get_unit_display()
        if self.unit == 'unit':
            return f"{self.amount} {self.name}"
        return f"{self.amount} {unit} {self.name}"
    