from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'priority', 'due_day', 'status']
        widgets = {
            'due_day': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(),  # For dropdown choices
            'priority': forms.Select(),  # For dropdown priority
        }