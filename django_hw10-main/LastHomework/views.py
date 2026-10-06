from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Reader

def is_librarian(user):
    return user.is_staff or not user.groups.filter(name='Readers').exists()

@login_required
def book_list(request):
    mode = request.GET.get('mode', 'all') # Отримуємо режим з URL: ?mode=available
    
    if mode == 'available':
        books = Book.objects.filter(holder__isnull=True)
    else:
        books = Book.objects.all()
        
    return render(request, 'library/book_list.html', {'books': books, 'mode': mode})

@login_required
@user_passes_test(is_librarian)
def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'library/reader_list.html', {'readers': readers})

@login_required
@user_passes_test(is_librarian)
def reader_detail(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    borrowed_books = reader.borrowed_books.all() 
    return render(request, 'library/reader_detail.html', {
        'reader': reader,
        'borrowed_books': borrowed_books
    })