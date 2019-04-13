from django.shortcuts import render
from django.http import HttpResponseRedirect,  HttpResponse
from .models import Author
from books.models import Book

# Create your views here.
def  authdetails(request,value):
   
    authi = Author.objects.get(auth_name= value)
    b =  Book.objects.filter(author_id = authi)
    context = { "author" : Author.objects.get(auth_name= value),
                "books" : Book.objects.filter(author_id = authi)
    }
    return render(request, "authors/index.html", context )