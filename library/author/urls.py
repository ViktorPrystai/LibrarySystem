from django.urls import path
from .views import author_list, author_create, author_delete

urlpatterns = [
    path('authors/', author_list, name='author_list'),
    path('authors/create/', author_create, name='author_create'),
    path('authors/<int:author_id>/delete/', author_delete, name='author_delete'),
]