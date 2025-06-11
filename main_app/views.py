from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Create your views here.

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def recipe_index(request):
    # Render the recipes/index.html with the data
    return render(request, 'recipes/index.html', {'recipes': recipes })