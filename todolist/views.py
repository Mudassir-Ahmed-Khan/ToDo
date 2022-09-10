from multiprocessing import context
from django.template import loader
from .forms import PersonDetailsFrom, TaskDetailsFrom
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Person, Task
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect



# Create your views here.
def home(request):
    return HttpResponse("Django!")

def description(request):
    i=3
    i=i+1
    return HttpResponse("I am django i am a very good website development framework %s" %i)


def description_number(request, number):

    return HttpResponse("My description number is %s" % number)




def add_person(request):
    context ={}
    form = PersonDetailsFrom(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form']= form
    return render(request, "todolist/person_details_form.html", context)



def add_task(request):
    context = {}
    task_details_form = TaskDetailsFrom(request.POST or None)
    if task_details_form.is_valid():
        task_details_form.save()

    context['task_details_form'] = task_details_form
    return render(request, "todolist/task_details_form.html", context)

def delete_task(request, id):
    context = {}
    obj = get_object_or_404(Task, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/task/<int:id>/")
    return render(request, "todolist/delete_tasks.html", context)




def users(request):
    users_set = list(Person.objects.all())
    # try:
    #     users_set = list(Person.objects.all())
    # except Person.DoesNotExist:
    #     raise Http404("Person is not available")
    return render(request, 'todolist/index.html', {'users_set': users_set})


def display_task(request, number):
    context = {}
    task_per_person = Task.objects.filter(person_id = number)
    return render(request, "todolist/tasks_per_person.html", {'task_per_person':task_per_person})

