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

    def clean_due_day(self):
        """
        Checks if the due_day is valid (not in the past)
        """
        due_day = self.cleaned_data.get('due_day')
        today = date.today()
        if due_day < today:
            raise forms.ValidationError('You cannot choose a date in the past.')
        return due_day