from multiprocessing import context
from django.contrib import messages
from django.template import loader
from .forms import PersonDetailsFrom, TaskDetailsFrom, GeeksForm
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from .models import *
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect



# Create your views here.
def home(request):
    return HttpResponse("Django!")





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
    if request.method == "POST":
        obj.delete()
        # messages.info("item removed !!!")
        return HttpResponseRedirect("/display_task/")

def update_task(request, task_id):
    context ={}
    obj = get_object_or_404(Task, id = task_id)
    update_task_form = TaskDetailsFrom(request.POST or None, instance = obj)
    if update_task_form.is_valid():
        update_task_form.save()
        return HttpResponseRedirect("/display_task/")
    context["update_task_form"] = update_task_form
    return render(request, "todolist/update.html", context)

def insert_user(request):
    # if request.method == 'POST':
    user_detail_form = PersonDetailsFrom(request.POST or None)
    if user_detail_form.is_valid():
        user_detail_form.save()
        return HttpResponseRedirect("/display_user/")
    return render(request, 'todolist/insert.html', {'user_detail_form' : user_detail_form})


def display_user(request):
    users_set = list(Person.objects.all())
    return render(request, 'todolist/show.html', {'users_set': users_set})


def delete_user(request):
    
    if request.method == 'POST':
        return render(request, 'todolist/delete.html')


def sum(request):
    return render(request, 'todolist/sum.html')

def result(request):
    Number1=int(request.POST["num1"])
    print(Number1)
    Number2=int(request.POST["num2"])
    print(Number2)
    res= Number1+Number2
    return HttpResponse(res)

# def detail_view(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
  
#     # add the dictionary during initialization
#     context["data"] = GeeksModel.objects.get(id = id)
          
#     return render(request, "todolist/detail.html", context)
 
# update view for details




