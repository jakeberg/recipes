from django import forms
from .models import Recipe, Author


class RecipeFrom(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "body",
            "author"
        ]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            "name"
        ]
