from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name=models.CharField(max_length=255)
    bio=models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        ordering=["name"]

class Book(models.Model):
    author=models.ForeignKey(Author,related_name='Authors',on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/", default=None)
    price=models.FloatField()
    description=models.TextField()

    def __str__(self):
        return self.title


class Purchases(models.Model):
    book=models.ForeignKey(Book, related_name="Books", on_delete=models.CASCADE)
    customer=models.ForeignKey(User, related_name="Customers", on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField()

    def __str__(self):
        return self.book.title