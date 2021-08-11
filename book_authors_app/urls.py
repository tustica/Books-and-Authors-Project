from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('author', views.author),
    path('add-book', views.add_book),
    path('add-author-name', views.add_author_name),
    path('books-view/<int:number>', views.books_view),
    path('add-author/<int:number>', views.add_author),
]