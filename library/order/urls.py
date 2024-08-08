from django.urls import path
from . import views

urlpatterns = [
    path('my-orders/', views.my_orders_view, name='my_orders'),
    path('create-order/', views.create_order_view, name='create_order'),
    path('close-order/<int:order_id>/', views.close_order_view, name='close_order'),
    path('all-orders/', views.all_orders_view, name='all_orders'),
]