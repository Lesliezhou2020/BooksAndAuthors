from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.create_books),
    path('authors', views.author_index),
    path('author/create', views.create_authors),
    path('books/<int:book_id>', views.books),
    path('authors/<int:author_id>', views.authors),
    path('authors/add/<int:book_id>', views.add_authors),
    path('books/add/<int:author_id>', views.add_books),
    
]