from django.urls import path
from todolist import views
import debug_toolbar
import todolist
app_name = 'todolist'

urlpatterns = [
    path("", views.insert_user, name = 'insert_user'),
    path("display_user/", views.display_user, name = 'display_user'),
    path('delete_user/', views.delete_user, name = 'delete_user'),
    path('hello/', views.home),
    path('display_task/', views.display_task, name = 'display_task'),
    path("delete_task/<task_id>/", views.delete_task, name = 'delete_task'),
    path("update_task/<task_id>/", views.update_task, name = 'update_task'),
    path("sum/",views.sum, name = "sum"),
    path("result/",views.result, name = "result"),
    # path('<id>/', views.detail_view ),
    # path('<id>/update', views.update_view ),
]



