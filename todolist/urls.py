from django.urls import path
from todolist import views
import debug_toolbar

urlpatterns = [
    path('hello/', views.home),
    path('description/', views.description),
    path('description/<int:number>/', views.description_number),
    path('premium_members/<int:number>/', views.premium_members)
]