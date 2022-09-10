from django import forms
from .models import Task, Person

class PersonDetailsFrom(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class TaskDetailsFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"




