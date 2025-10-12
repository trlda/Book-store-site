from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Authors_name')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='Publisher_name')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='Genre_name')
    rating = models.DecimalField(decimal_places=2, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=10)