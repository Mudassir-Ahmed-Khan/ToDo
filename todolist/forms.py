from django import forms
from .models import Task, Person
from .models import GeeksModel

class PersonDetailsFrom(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class TaskDetailsFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


 
 
# creating a form
class GeeksForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel
 
        # specify fields to be used
        fields = [
            "title",
            "description"]



