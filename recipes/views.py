from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.shortcuts import get_object_or_404

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return  render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
def recipe(request, id):
    recipe_obj = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe_obj,
        'is_detail_page': True,
    })
    
