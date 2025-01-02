from datetime import date

from django.contrib import messages
from django.http import JsonResponse, HttpResponse, Http404
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View, TemplateView
from .forms import *
from library.models import *


# Create your views here.
def square_view(request):
    number = request.GET.get('number')
    if not number or not number.isdigit():
        return JsonResponse({'error': 'Invalid number'}, status=400)

    number = int(number)
    cache_key = f'square-{number}'

    square = cache.get(cache_key)
    if square is not None:
        return JsonResponse({'number':number, 'square': square, 'cached': True})

    square = number ** 2
    cache.set(cache_key, square, timeout=60 * 5)
    return JsonResponse({'number':number, 'square': square, 'cached': False})




class HomeView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        context = {'books': books}

        return render(request, self.template_name, context)



class ProfileView(TemplateView):
    template_name = 'userprofile.html'
    
    def get(self, request, *args, **kwargs):
        try:
            userprofile = get_object_or_404(Profile, user=request.user)

        except Profile.DoesNotExist:
            raise Http404(
                "No profile found for this user.")
        print(f"User Profile: {userprofile}")

        return render(request, 'userprofile.html', {'userprofile': userprofile})



class AuthorListView(ListView):
    model = Author
    fields = '__all__'
    context_object_name = 'authors'
    template_name = 'author_list.html'

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    context_object_name = 'author_create'
    template_name = 'author_create.html'
    success_url = reverse_lazy('author_list')

class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    context_object_name = 'author_detail'
    template_name = 'author_detail.html'

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    context_object_name = 'author_update'
    template_name = 'author_update.html'
    success_url = reverse_lazy('author_list')


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    context_object_name = 'author_delete'
    template_name = 'confirm_author_delete.html'
    success_url = reverse_lazy('author_list')

class PublisherListView(ListView):
    model = Publisher
    fields = '__all__'
    context_object_name = 'publishers'
    template_name = 'publisher_list.html'

class PublisherCreateView(LoginRequiredMixin, CreateView):
    model = Publisher
    fields = '__all__'
    context_object_name = 'publisher_create'
    template_name = 'publisher_create.html'
    success_url = reverse_lazy('publisher_list')

class PublisherDetailView(LoginRequiredMixin, DetailView):
    model = Publisher
    context_object_name = 'publisher_detail'
    template_name = 'publisher_detail.html'

class PublisherUpdateView(LoginRequiredMixin, UpdateView):
    model = Publisher
    fields = '__all__'
    context_object_name = 'publisher_update'
    template_name = 'publisher_update.html'
    success_url = reverse_lazy('publisher_list')

class PublisherDeleteView(LoginRequiredMixin, DeleteView):
    model = Publisher
    context_object_name = 'publisher_delete'
    template_name = 'confirm_publisher_delete.html'
    success_url = reverse_lazy('publisher_list')

class GenreListView(ListView):
    model = Genre
    fields = '__all__'
    context_object_name = 'genres'
    template_name = 'genre_list.html'

class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    fields = '__all__'
    context_object_name = 'genre_create'
    template_name = 'genre_create.html'
    success_url = reverse_lazy('genre_list')

class GenreDetailView(LoginRequiredMixin, DetailView):
    model = Genre
    context_object_name = 'genre_detail'
    template_name = 'genre_detail.html'

class GenreUpdateView(LoginRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    context_object_name = 'genre_update'
    template_name = 'genre_update.html'
    success_url = reverse_lazy('genre_list')

class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    context_object_name = 'genre_delete'
    template_name = 'confirm_genre_delete.html'

class BookListView(ListView):
    model = Book
    fields = '__all__'
    context_object_name = 'books'
    template_name = 'book_list.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    context_object_name = 'book_create'
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list')

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book_detail'
    template_name = 'book_detail.html'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    context_object_name = 'book_update'
    template_name = 'book_update.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    context_object_name = 'book_delete'
    template_name = 'confirm_book_delete.html'
    success_url = reverse_lazy('book_list')

class BorrowListView(ListView):
    model = Borrow
    fields = '__all__'
    context_object_name = 'borrows'
    template_name = 'borrow_list.html'

class BorrowCreateView(LoginRequiredMixin, CreateView):
    model = Borrow
    form_class = BorrowForm
    context_object_name = 'borrow_create'
    template_name = 'borrow_create.html'
    success_url = reverse_lazy('borrow_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BorrowCreateViewbyID(LoginRequiredMixin, CreateView):
    model = Borrow
    form_class = BorrowFormbyID
    context_object_name = 'borrow_create_by_id'
    template_name = 'borrow_create_by_id.html'
    success_url = reverse_lazy('borrow_list')

    # def get_initial(self):
    #     initial = super().get_initial()
    #     book = get_object_or_404(Book, id=self.kwargs['book_id'])
    #     initial['book'] = book
    #     return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        book = get_object_or_404(Book, id=self.kwargs['book_id'])
        form.instance.book = book
        return super().form_valid(form)


class BorrowDetailView(LoginRequiredMixin, DetailView):
    model = Borrow
    context_object_name = 'borrow_detail'
    template_name = 'borrow_detail.html'

class BorrowUpdateView(LoginRequiredMixin, UpdateView):
    model = Borrow
    fields = '__all__'
    context_object_name = 'borrow_update'
    template_name = 'borrow_update.html'
    success_url = reverse_lazy('borrow_list')

class BorrowDeleteView(LoginRequiredMixin, DeleteView):
    model = Borrow
    context_object_name = 'borrow_delete'
    template_name = 'confirm_borrow_delete.html'
    success_url = reverse_lazy('borrow_list')



def manage_borrows(request):

    # if not request.user.is_superuser:
    #     return HttpResponse("You are not authorized to view this page.")
    if not request.user.is_staff:
        messages.error(request, 'You are not authorized to view this page.')
        return redirect('login')

    borrows = Borrow.objects.all()
    if 'end' in request.POST:
        borrow = get_object_or_404(Borrow, id=request.POST['end'])
        borrow.book.quantity += 1
        borrow.book.save()
        borrow.delete()

    context = {'borrows': borrows}
    return render(request, 'manage_borrows.html', context)