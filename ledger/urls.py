from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipeslist", views.recipesPage, name="recipesPage"),
    path("recipe1", views.recipes1, name="recipe1"),
    path("recipe2", views.recipes2, name="recipe2"),
    path("login", views.loginpage, name="login"),
    path("recipe/add", views.recipe_create, name="recipemaking"),
    path("recipe/<int:pk>", views.recipe_detail, name="recipe_detail")

]

