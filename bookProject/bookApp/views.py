from django.shortcuts import redirect, render
from bookApp.models import *

def index(request):
    context = {
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all(),

    }
    return render(request, 'index.html', context)

def create_books(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
    )
    
    return redirect('/')

def books(request, book_id):
    book = Book.objects.get(id=book_id)
    context={
        'book': book,
        'authors': book.authors.all(),
        'all_authors': Author.objects.all(),
    }
    return render(request, 'desc.html', context )

def author_index(request):
    context ={
        'all_books': Book.objects.all(),
        'all_authors': Author.objects.all(),
    }
    return render(request, 'authors.html', context)


def create_authors(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name =request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect('/authors')

def authors(request, author_id):
    author = Author.objects.get(id=author_id)
    context={
        'author': author,
        'all_books': Book.objects.all(),  
        'books': author.books.all(),
    }
    return render(request, 'last.html', context)

def add_authors(request, book_id):
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id = request.POST['author_id'])
    author.books.add(book)
    return redirect('/books/{}'.format(book_id))

def add_books(request, author_id):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = author_id)
    book.authors.add(author)    
    return redirect('/authors/{}'.format(author_id))




