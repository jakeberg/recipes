from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from recipes.models import Recipe
from .forms import RecipeFrom, AuthorForm


def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes.html', { 'recipes': recipes, 'page_title': 'All recipes'})


def recipe_details_views(request, key):
    recipes = Recipe.objects.get(id=key)
    return render(request, 'recipe_details.html', { 'recipes': recipes })


def recipe_create_view(request):
    form = RecipeFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, 'recipe_form.html', {'form': form})


def author_detail_view(request, id):
    recipes = Recipe.objects.filter(author__id=id)
    data = {
        'recipes': recipes, 
        'page_title': 'Author recipes',
    }
    return render(request, 'recipes.html', data)

def author_create_view(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, 'author_form.html', {'form': form})
