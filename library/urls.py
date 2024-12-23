from django.urls import path

from library.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authorlist/',AuthorListView.as_view(), name='author_list'),
    path('authorcreate/', AuthorCreateView.as_view(), name='author_create'),
    path('authordetail/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authorupdate/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('authordelete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),
    path('publisherlist/', PublisherListView.as_view(), name='publisher_list'),
    path('publishercreate/', PublisherCreateView.as_view(), name='publisher_create'),
    path('publisherdetail/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
    path('publisherupdate/<int:pk>/', PublisherUpdateView.as_view(), name='publisher_update'),
    path('publisherdelete/<int:pk>/', PublisherDeleteView.as_view(), name='publisher_delete'),
    path('genrelist/', GenreListView.as_view(), name='genre_list'),
    path('genrecreate/', GenreCreateView.as_view(), name='genre_create'),
    path('genredetail/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('genreupdate/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genredelete/<int:pk>/', GenreDeleteView.as_view(), name='genre_delete'),
    path('booklist/', BookListView.as_view(), name='book_list'),
    path('bookcreate/', BookCreateView.as_view(), name='book_create'),
    path('bookdetail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('bookupdate/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('bookdelete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('borrowlist/', BorrowListView.as_view(), name='borrow_list'),
    path('borrowcreate/', BorrowCreateView.as_view(), name='borrow_create'),
    path('borrow/create/<int:book_id>/', BorrowCreateViewbyID.as_view(), name='borrow_create_by_id'),
    path('borrowdetail/<int:pk>/', BorrowDetailView.as_view(), name='borrow_detail'),
    path('borrowupdate/<int:pk>/', BorrowUpdateView.as_view(), name='borrow_update'),
    path('borrowdelete/<int:pk>/', BorrowDeleteView.as_view(), name='borrow_delete'),



]