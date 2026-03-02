from django.contrib import admin
from .models import Profile, Ingredient, Recipe, RecipeIngredient

admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)

# Register your models here.

