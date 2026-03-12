from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    userkey = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    p_name = models.CharField(max_length = 50)
    p_shortbio = models.TextField()

class Ingredient(models.Model):
    ing_name = models.CharField(max_length=30)

class Recipe(models.Model):
    reci_name = models.CharField(max_length=30)
    author = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    CreatedOn = models.DateTimeField(auto_now_add=True,null=True)
    UpdatedOn = models.DateTimeField(auto_now=True,null=True)

class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    reci_ing = models.ForeignKey(Ingredient, default=None, on_delete=models.CASCADE)
    recipefield = models.ForeignKey(Recipe, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.ing_name
    
class RecipeImage(models.Model):
    image = models.ImageField(
        upload_to = "media/",
        blank = False,
        null = True
    )
    description = models.TextField(
        max_length=255
    )
    recipe_key = models.ForeignKey(
        Recipe,
        null=True,
        on_delete=models.CASCADE,
        related_name="images"
    )


# Create your models here.


