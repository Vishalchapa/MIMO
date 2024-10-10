from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard view handles creation and editing
    path('task/<int:task_id>/edit/', views.dashboard, name='task-edit'),  # Edit Task
    path('task/<int:task_id>/delete/', views.delete_task, name='task-delete'),  # Delete Task
    path('task/<int:task_id>/complete/', views.mark_as_complete, name='task-complete'),  # Mark as complete
    path('task/<int:task_id>/change-priority/', views.change_priority, name='change-priority'),
    path('task/<int:task_id>/change-status/', views.change_status, name='change-status'),
]