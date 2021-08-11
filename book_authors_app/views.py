from django.http.response import HttpResponse
from book_authors_app.models import Author, Book
from django.shortcuts import redirect, render

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def author(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)

def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def add_author_name(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect('/author')


def add_author(request, number):
    Book.objects.get(id=number).authors.add(Author.objects.get(id=request.POST['add_author']))
    return redirect('/books-view/'+ str(number))

def books_view(request, number):
    context = {
        "book": Book.objects.get(id=number),
        "authors": Book.objects.get(id=number).authors.all(),
        "all_authors": Author.objects.all()
    }
    return render(request, 'books.html', context)