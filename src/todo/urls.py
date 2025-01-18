from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('mark_completed/<int:task_id>', views.mark_completed, name='mark_completed'),
]
