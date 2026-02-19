from django.shortcuts import render
from django.http import HttpResponse
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

# def recipeslist(request):
#     html = """
#     <html>
#         <body>
#             <h1>Recipe Book</h1>
#             <h2>Links</h2>
#             <ul>
#                 <li><a href="http://127.0.0.1:8000/ledger/recipe/1"> Recipe 1 </a></li>
#                 <li><a href="http://127.0.0.1:8000/ledger/recipe/2"> Recipe 2 </a></li>
#             </ul>
#         </body>
#     </html>
#     """
#     return HttpResponse(html)

# def recipe1(request):
#     html = """
#     <html>
#         <body>
#             <h1>Recipe Book</h1>
#             <h2>Ingredients</h2>
#             <ul>
#                 <li>tomato (3pcs)</li>
#                 <li>onion (1pc)</li>
#                 <li>pork (1kg)</li>
#                 <li>water (1L)</li>
#                 <li>sinigang mix (1 packet)</li>
#             </ul>
#         </body>
#     </html>
#     """
#     return HttpResponse(html)

# def recipe2(request):
#     html = """
#     <html>
#         <body>
#             <h1>Recipe Book</h1>
#             <h2>Ingredients</h2>
#             <ul>
#                 <li>garlic (1 head)</li>
#                 <li>onion (1pc)</li>
#                 <li>vinegar (1/2 cup)</li>
#                 <li>water (1 cup)</li>
#                 <li>salt (1 tbsp)</li>
#                 <li>whole black peppers (1 tbsp)</li>
#                 <li>pork (1 kilo)</li>
#             </ul>
#         </body>
#     </html>
#     """
#     return HttpResponse(html)

# Create your views here.
