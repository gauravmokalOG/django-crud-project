from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # List all items
    path('item/<int:pk>/', views.item_detail, name='item_detail'),  # View details of a single item
    path('create/', views.create_item, name='create_item'),  # Create a new item
    path('update/<int:pk>/', views.update_item, name='update_item'),  # Update an item
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),  # Delete an item
]
