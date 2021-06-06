from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    # path('books/upload/', views.upload_book, name='upload_book'),
    # path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    # url(r'^books/$', views.search, name='book_list'),
    # path('books/', views.search, name='book_list'),
    # path("books/", views.Search.as_view(), name='book_list'),
    # path('books2/', views.search, name='book_list2'),
    

    #path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    #path('books/inf', views.BookListView2.as_view(), name= 'book_list2'),
    #path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
