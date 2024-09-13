from django.urls import path
from . import views

urlpatterns = [
    path('my-orders/', views.my_orders_view, name='my_orders'),
    path('create-order/', views.create_order_view, name='create_order'),
    path('order/request-close/<int:order_id>/', views.request_close_order, name='request_close_order'),
    path('order/close/<int:order_id>/', views.close_order, name='close_order'),
    path('order/<int:order_id>/detail/', views.order_detail, name='order_detail'),
    path('order/confirm/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('books/<int:book_id>/get-title/', views.get_book_title, name='get_book_title'),
    path('all-orders/', views.all_orders_view, name='all_orders'),
]