from multiprocessing import context
from django.contrib import messages
from django.template import loader
from .forms import PersonDetailsFrom, TaskDetailsFrom
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from .models import Person, Task
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect



# Create your views here.
def home(request):
    return HttpResponse("Django!")


def users(request):
    users_set = list(Person.objects.all())
    return render(request, 'todolist/index.html', {'users_set': users_set})


def add_user(request):
    context ={}
    form = PersonDetailsFrom(request.POST or None)
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/")
    context['form']= form
    return render(request, "todolist/index.html", context)





def display_task(request):
    task_per_person = list(Task.objects.filter(person_id = 1))
    user_name = Person.objects.get(pk = 1)
    task_details_form = TaskDetailsFrom(request.POST or None)
    if task_details_form.is_valid():
        task_details_form.save()
        return HttpResponseRedirect("/display_task/")
    data_to_display = {'task_per_person':task_per_person, 'user_name':user_name, 'task_details_form':task_details_form}
    return render(request, 'todolist/index.html',data_to_display)

def delete_task(request, task_id):
    obj = Task.objects.get(id=task_id)
    # if request.method == "POST":
    obj.delete()
    # messages.info("item removed !!!")
    return HttpResponseRedirect("/display_task/")


def display_form(request):
    return render(request, 'todolist/add.html')


def add(request):
    val1 = int(request.POST["number1"])
    val2 = int(request.POST["number2"])
    result = val1+val2
    return render(request, 'todolist/add.html', {'result': result})



