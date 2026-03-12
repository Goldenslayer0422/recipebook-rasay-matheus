from django.contrib import admin
from .models import Profile, Ingredient, Recipe, RecipeIngredient, RecipeImage

admin.site.register(Profile)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeImage)

# Register your models here.


