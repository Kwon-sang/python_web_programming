from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Book, Author, Publisher


# Template View
class BookModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


# List View
class BookList(ListView):
    model = Book
    template_name = 'books/list/book_list.html'

class AuthorList(ListView):
    model = Author
    template_name = 'books/list/author_list.html'

class PublisherList(ListView):
    model = Publisher
    template_name = 'books/list/publisher_list.html'


# Detail View
class BookDetail(DetailView):
    model = Book
    template_name = 'books/detail/book_detail.html'

class AuthorDetail(DetailView):
    model = Author
    template_name = 'books/detail/author_detail.html'

class PublisherDetail(DetailView):
    model = Publisher
    template_name = 'books/detail/publisher_detail.html'

