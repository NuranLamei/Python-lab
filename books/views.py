from django.shortcuts import render
from .models import Book , Comment
from django.http import HttpResponseRedirect,  HttpResponse
from .forms import AddBookForm
from django.shortcuts import render
# Create your views here.
def  index(request):
    context = { "book" : Book.objects.all()}
    return render(request, "books/index.html", context )

def bookdetails(request, name):
    form = AddBookForm(request.POST)
    
    if request.method=="POST":
        if form.is_valid():
           mybook = Book.objects.get(title=name)
           Comment.objects.create(text= request.POST['title'], user= request.POST['email'] , book= mybook)
           
           comments = Comment.objects.filter(book = mybook)
           context = {"book" : mybook,'comments' : comments, "form": form}
           return render(request,"books/bookdetails.html", context )
    else:
        for book in Book.objects.all():
            if book.title == name:
                comments1 = Comment.objects.filter(book = book)
                context = {"book" : book,'comments' : comments1, "form": form}
    return render(request,"books/bookdetails.html", context )
       



