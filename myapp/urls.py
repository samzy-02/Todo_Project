from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('editTodo/<int:pk>/',views.editTodo, name='editTodo'),
]
