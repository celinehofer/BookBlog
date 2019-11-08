from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


# Definition Felder für Bucheinträge
class Book(models.Model):
    title = models.CharField(max_length=255, null=True, default='')
    author = models.CharField(max_length=255, null=True, default='')
    genre = models.CharField(max_length=255, null=True, default='')
    description = models.CharField(max_length=3000, null=True, default='')
    review = models.CharField(max_length=3000, null=True, default='')

    # Zeigt Titel und Author im Admin-Login
    def __str__(self):
        return self.title + ", " + self.author


# Definition der Felder für Kommentare
class Comment(models.Model):
    text = models.CharField(max_length=1000, null=True, default='')
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # Zeigt ID und User im Admin-Login
    def __str__(self):
        return f"{self.id} - {self.user}"
