from django import forms
from .models import Recipe, Author


class RecipeForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        if user.is_staff is False:
            a = Author.objects.filter(user=user).first()
            self.fields['author'].choices = [(a.id, a.name)]

    class Meta:
        model = Recipe
        fields = [
            "title",
            "body",
            "author"
        ]


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

