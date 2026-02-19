from django.db import models

class Ingredient(models.Model):
    ing_name = models.CharField(max_length=30)

class Recipe(models.Model):
    reci_name = models.CharField(max_length=30)

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    reci_ing = models.ForeignKey(Ingredient, default=None, on_delete=models.CASCADE)
    recipefield = models.ForeignKey(Recipe, default=None, on_delete=models.CASCADE)

def __str__(self):
    return self.ing_name


# Create your models here.
