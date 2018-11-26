from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import Recipe


def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', { 'recipes': recipes, 'page_title': 'All recipes'})


def recipe_details_views(request, key):
    recipes = Recipe.objects.get(id=key)
    return render(request, 'recipe_details.html', { 'recipes': recipes })

def authors_detail_view(request, id):
    recipes = Recipe.objects.filter(author__id=id)
    data = {
        'recipes': recipes, 
        'page_title': 'Author recipes',
    }
    return render(request, 'recipes.html', data)