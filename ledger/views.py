from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage, Profile
from .forms import RecipeForm, ImageForm


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

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe_detail.html", {"recipe": recipe})

def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = Profile.objects.get(p_name=request.user) 

            recipe.save()
            return redirect("recipe_detail", pk=recipe.pk) 
    else:
        form = RecipeForm()
    return render(request, "recipemaker.html", {"form": form})

def add_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe_key = recipe
            recipe_image.save()
            return redirect("recipe_detail", pk=recipe.pk)
    else:
        form = ImageForm()
    return render(request, "recipeimager.html", {"form": form, "recipe": recipe})

# Create your views here.


