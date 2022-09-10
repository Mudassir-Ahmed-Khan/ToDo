from django.urls import path
from todolist import views
import debug_toolbar

import todolist

app_name = 'todolist'
urlpatterns = [
    path('hello/', views.home),
    path("", views.add_person),
    path("add_task/", views.add_task),
    path('description/', views.description),
    path('description/<int:number>/', views.description_number, name = 'description'),
    path('users/', views.users),
    path('task/<int:number>/', views.display_task, name = 'display_task'),
    path('<int:id>/delete/', views.delete_task, name = 'delete_task'),
]



