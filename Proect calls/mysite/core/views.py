from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Length, Upper, Lower
from .forms import BookForm
from .models import Book
from .filters import BookFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



class Home(TemplateView):
    template_name = 'home.html'
 # Расширяем базовый клас,чтобы он также отображал шаблон.


def book_list(request):
    posts_list = Book.objects.order_by('-id')
    query = request.GET.get('q')
    if query:
        posts_list = Book.objects.filter(
            Q(TimeStartJ__icontains=query) | Q(Tel1B__icontains=query) |
            Q(Tel2C__icontains=query) | Q(KtoE__icontains=query)
        ).distinct().order_by('-id')
    paginator = Paginator(posts_list, 20)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }

    return render(request, "book_list.html", context)






# {{ filter.form.as_p }} {% for book in page.qs  %}
#
# def book_list(request):
#     book_set = Book.objects.order_by('-id')
#     paginator = Paginator(book_set, 25)
#     page_number = request.GET.get('page')
#     contacts = paginator.get_page(page_number)
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = BookFilter
#     # book_filter = BookFilter(request.GET, queryset=book_set)
#     return render(request, 'book_list.html', {'page': contacts})
# # {'filter': page_number})   {{ page.form.as_p }}  {% for book in filter.qs  %}
#  # Получаем объекты из таблицы для нужного нам договора.

def book_detail(reqest, pk):
    book = Book.objects.get(pk=pk)
    return render(reqest, 'book_detail.html',{'book' : book} )



#
# def book_list(request):
#     # books = Book.objects.all()
#     # return render(request, 'book_list.html', {
#     #     'books': books
#     # })
#     # .order_by('-id')
#     book_set = Book.objects.order_by('-id')
#     paginator = Paginator(book_set, 25)
#     page_number = request.GET.get('page')
#     contacts = paginator.get_page(page_number)
#     # page_number = BookFilter(request.GET.get('page'))
#     # page = paginator.get_page(page_number)
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = BookFilter
#     book_filter = BookFilter(request.GET, queryset=book_set)
#     return render(request, 'book_list.html', {'search': book_filter, 'page': contacts})
