from django import forms
from .models import Recipe, Author


class RecipeFrom(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(RecipeFrom, self).__init__(*args, **kwargs)
        if user.is_staff is False:
            self.fields['author'].choices = [(user.id, user.username)]
        
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


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

