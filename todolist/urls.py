from django.urls import path, include
from todolist import views

urlpatterns = [
    path('hello/', views.home),
    
]