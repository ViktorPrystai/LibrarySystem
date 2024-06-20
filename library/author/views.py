from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Author

def is_librarian(user):
    return user.role == 1

@login_required
@user_passes_test(is_librarian)
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author/author_list.html', {'authors': authors})

@login_required
@user_passes_test(is_librarian)
def author_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        author = Author(name=name, surname=surname, patronymic=patronymic)
        author.save()
        return redirect('author_list')
    return render(request, 'author/author_create.html')

@login_required
@user_passes_test(is_librarian)
def author_delete(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if not author.books.exists():
        author.delete()
        return redirect('author_list')
    return render(request, 'author/author_list.html', {'authors': Author.objects.all(), 'error': 'Cannot delete author attached to a book'})
