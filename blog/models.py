from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, default='')
    author = models.CharField(max_length=255, null=True, default='')
    genre = models.CharField(max_length=255, null=True, default='')
    description = models.CharField(max_length=3000, null=True, default='')
    #rating = models.IntegerField
    review = models.CharField(max_length=3000, null=True, default='')

    # show title, url and user in admin-login
    def __str__(self):
        return self.title + ", " + self.author


class Comment(models.Model):
    text = models.CharField(max_length=1000, null=True, default='')
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # show id, book and user in admin-login
    def __str__(self):
        return f"{self.id} - {self.user}"