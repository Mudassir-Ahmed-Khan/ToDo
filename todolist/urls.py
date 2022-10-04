from django.urls import path
from todolist import views
import debug_toolbar
import todolist
app_name = 'todolist'

urlpatterns = [
    path("", views.display_form, name = 'display_form'),
    path('hello/', views.home),
    path('display_task/', views.display_task, name = 'display_task'),
    path("delete_task/<task_id>/", views.delete_task, name = 'delete_task'),
    path("add/", views.add, name = 'add'),
]



