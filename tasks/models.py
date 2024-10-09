from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

PRIORITY_CHOICES = (
    ("High", "High"),
    ("Normal", "Normal"),
    ("Low", "Low")
)

STATUS_CHOICES = [
        (0, 'Not Started'),
        (1, 'In Progress'),
        (2, 'Completed'),
    ]

class Task(models.Model):
    
    """
    Task model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user")
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(max_length=5000, null=True, blank=True)
    priority = models.CharField(
            max_length=50,
            choices=PRIORITY_CHOICES,
            default="Normal"
            )
    due_day = models.DateField(default=datetime.now, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title
