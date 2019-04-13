from django.db import models
from authors.models import Author

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    bid = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(Author, blank=True, null=True,on_delete = models.SET_NULL)
    
class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.CharField(max_length=100)
    book = models.ForeignKey(Book,blank=True, null=True, on_delete=models.SET_NULL)