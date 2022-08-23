from turtle import title
from django.db import models

# Create your models here.
class User(models.Model):
    SUBSCRIPTION_TYPE = (
        ('F', 'Free'),
        ('C', 'Classic'),
        ('P', 'Premium')
    )
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    subscription_type = models.CharField(max_length = 1, choices = SUBSCRIPTION_TYPE)
    joined_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    TASK_TYPE = (
        ('P', 'Personal'),
        ('E', 'Educational'),
        ('W', 'Work')
    )

    TASK_STATUS = (
        ('C', 'Complete'),
        ('P', 'Pending'),
    )

    TASK_PRIORITY = (
        ('L','Low'),
        ('M', 'Medium'),
        ('H', 'High')
    )
    
    description = models.TextField()
    task_status = models.CharField(max_length=1, choices = TASK_STATUS)
    task_priority = models.CharField(max_length=1, choices = TASK_PRIORITY)

