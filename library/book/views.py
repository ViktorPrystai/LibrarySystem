from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Book
from author.models import Author

def is_librarian(user):
    return user.is_authenticated and user.role == 1

def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    query = request.GET.get('q')
    author_id = request.GET.get('author')
    if query:
        books = books.filter(name__icontains=query)
    if author_id:
        books = books.filter(authors__id=author_id)
    return render(request, 'book/book_list.html', {'books': books, 'authors': authors})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

@login_required
@user_passes_test(is_librarian)
def add_book(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        count = request.POST['count']
        author_ids = request.POST.getlist('authors')
        authors = Author.objects.filter(id__in=author_ids)
        book = Book.objects.create(name=name, description=description, count=count)
        book.authors.set(authors)
        book.save()
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'book/add_book.html', {'authors': authors})
