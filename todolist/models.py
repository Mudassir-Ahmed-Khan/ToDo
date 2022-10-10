from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Person(models.Model):
    SUBSCRIPTION_TYPE = (
        ('F', 'Free'),
        ('C', 'Classic'),
        ('P', 'Premium')
    )
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    subscription_type = models.CharField(max_length = 1, choices = SUBSCRIPTION_TYPE)
    joined_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.first_name

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_status = models.CharField(max_length=1, choices = TASK_STATUS)
    task_priority = models.CharField(max_length=1, choices = TASK_PRIORITY)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

class Number(models.Model):
    Number1 = models.DecimalField(max_digits = 6, decimal_places = 2)
    Number2 = models.DecimalField(max_digits = 6, decimal_places = 2)

class GeeksModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title


