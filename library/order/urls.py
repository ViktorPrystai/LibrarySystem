from django.urls import path
from . import views

urlpatterns = [
    path('my-orders/', views.my_orders_view, name='my_orders'),
    path('create-order/', views.create_order_view, name='create_order'),
    path('order/request-close/<int:order_id>/', views.request_close_order, name='request_close_order'),
    path('order/close/<int:order_id>/', views.close_order, name='close_order'),
    path('order/confirm/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('all-orders/', views.all_orders_view, name='all_orders'),
]