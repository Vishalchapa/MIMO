from datetime import datetime, date
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_on']
        fields = ['title', 'body', 'priority', 'due_day', 'status']
        widgets = {
            'due_day': forms.DateInput(attrs={'type': 'date', 'id': 'id_due_day'}),
            'status': forms.Select(),  # For dropdown choices
            'priority': forms.Select(),  # For dropdown priority
        }
