from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from main.views import (
    TaskListsView, TaskListCreateView, TaskListUpdateView, TaskListDeleteView, 
    login_view, logout_view,
    TasksView, TaskCreateView, TaskUpdateView, TaskDeleteView
)


app_name = 'main'
urlpatterns = [
    path('', login_required(TaskListsView.as_view()), name='task_lists'),
    path('task_list_create/', login_required(TaskListCreateView.as_view()), name='task_list_create'),
    path('task_list_update/<int:pk>/', login_required(TaskListUpdateView.as_view()), name='task_list_update'),
    path('task_list_delete/<int:pk>/', login_required(TaskListDeleteView.as_view()), name='task_list_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('tasks/<int:task_list_id>/', login_required(TasksView.as_view()), name='tasks'),
    path('task_create/<int:task_list_id>/', login_required(TaskCreateView.as_view()), name='task_create'),
    path('task_update/<int:pk>/<int:task_list_id>/', login_required(TaskUpdateView.as_view()), name='task_update'),
    path('task_delete/<int:pk>/<int:task_list_id>/', login_required(TaskDeleteView.as_view()), name='task_delete')
]