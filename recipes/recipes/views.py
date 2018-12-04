from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from recipes.models import Recipe, Author
from recipes.forms import RecipeForm, SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse

def signup_view(request):

    html = "signup.html"

    form = SignupForm(None or request.POST)

    if form.is_valid():
        data = form.cleaned_data
        user = User.objects.create_user(
            data['username'], data['email'], data['password'])
        login(request, user)
        Author.objects.create(name=user.username, user=user)
        return HttpResponseRedirect(reverse('homepage'))

    if request.user.is_staff:
        return render(request, html, {'form': form})
    else:
        return HttpResponseRedirect(reverse('error'))

def login_view(request):

    html = "login.html"

    form = LoginForm(None or request.POST)
 
    if form.is_valid():
        next = request.POST.get('next')
        data = form.cleaned_data
        user = authenticate(username=data['username'], password=data['password'])
        
        if user is not None:
            login(request, user)  
        if next:
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect("/")

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def recipes_view(request):

    recipes = Recipe.objects.all()

    return render(request, 'recipes.html', { 'recipes': recipes, 'page_title': 'All recipes'})


def recipe_details_views(request, key):

    recipes = Recipe.objects.get(id=key)

    return render(request, 'recipe_details.html', { 'recipes': recipes })


@login_required()
def recipe_create_view(request):

    form = RecipeForm(request.user, request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'recipe_form.html', {'form': form})


@login_required()
def author_detail_view(request, id):

    recipes = Recipe.objects.filter(author__id=id)

    data = {
        'recipes': recipes, 
        'page_title': 'Author recipes',
        'author': recipes[0].author
    }
    return render(request, 'recipes.html', data)


def error_view(request):
    return render(request, 'error.html')