from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.title