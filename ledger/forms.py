from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["reci_name"]

class ImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ["image", "description"]