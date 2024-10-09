from django.contrib import admin
from .models import Task


# Register your models here.


@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'priority', 'due_day', 'status', 'created_on']
    list_filter = ['priority', 'status']
    search_fields = ['title', 'body']
    ordering = ['due_day']