from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Order
from book.models import Book


@login_required
def create_order_view(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        plated_end_at = request.POST.get('plated_end_at')


        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return render(request, 'create_order.html', {'error': 'Book does not exist.'})


        if book.count <= 0:
            return render(request, 'create_order.html', {'error': 'Book is not available.'})

        try:
            order = Order.objects.create(
                user=request.user,
                book=book,
                plated_end_at=plated_end_at
            )
            return redirect('my_orders')
        except Exception as e:
            return render(request, 'create_order.html', {'error': f'Error creating order: {str(e)}'})

    return render(request, 'create_order.html')

@login_required
def my_orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html', {'orders': orders})


@login_required
def close_order_view(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        order.end_at = timezone.now()
        order.save()
        return redirect('all_orders')
    except Order.DoesNotExist:
        return render(request, 'error.html', {'error': 'Order does not exist.'})


@login_required
def all_orders_view(request):
    orders = Order.objects.all()
    return render(request, 'all_orders.html', {'orders': orders})

