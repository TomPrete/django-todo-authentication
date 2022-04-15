from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new', views.new_task, name='new_task'),
    path('task/<int:task_id>', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),
]
