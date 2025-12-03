from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True) # Requirement
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium') # Requirement
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending') 
    completed_at = models.DateTimeField(null=True, blank=True) # Requirement: Timestamp
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-set timestamp when marked complete
        if self.status == 'Completed' and not self.completed_at:
            self.completed_at = timezone.now()
        elif self.status == 'Pending':
            self.completed_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
