from django.db import models

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
    ingredients = models.TextField(max_length=500)
    instructions = models.TextField(max_length=2000)

    def __str__(self):
        return  self.name
    