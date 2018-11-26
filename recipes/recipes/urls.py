"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from recipes.views import recipes_view, authors_detail_view, recipe_details_views
from django.urls import path
from recipes.models import Author, Recipe
admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', recipes_view),
    path('authors/<str:id>/', authors_detail_view),
    path('recipe/<int:key>/', recipe_details_views)
]
