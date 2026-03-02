from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Ingredient, Recipe, RecipeIngredient


def index(request):
    return HttpResponse("Hello, world. You're at the ledger index.")
    
def recipesPage(request):
    return render(request, 'recipeslist.html')
    
def recipes1(request):
    reciping1 = RecipeIngredient.objects.all()
    return render(request, 'recipes1.html', {'rec_ing1': reciping1})
    
def recipes2(request):
    reciping2 = RecipeIngredient.objects.all()
    return render(request, 'recipes2.html', {'rec_ing2': reciping2})
    
def loginpage(request):
    return render(request, 'login.html')

# Create your views here.

