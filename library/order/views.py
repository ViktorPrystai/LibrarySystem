from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseForbidden
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
def request_close_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user == order.user and order.status == 'open':
        order.status = 'pending'
        order.save()
        return redirect('my_orders')
    return HttpResponseForbidden("You are not allowed to close this order.")

@login_required
def close_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.role == 1:
        order.status = 'closed'
        order.save()
        return redirect('all_orders')
    return HttpResponseForbidden("Only librarians can close orders.")

@login_required
def confirm_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.role == 1 and order.status == 'pending':
        order.status = 'closed'
        order.save()
        return redirect('all_orders')
    return HttpResponseForbidden("You are not allowed to confirm this order.")

@login_required
def all_orders_view(request):
    orders = Order.objects.all()
    return render(request, 'all_orders.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

