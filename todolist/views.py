from multiprocessing import context
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Person, Task




# Create your views here.
def home(request):
    return HttpResponse("Django!")

def description(request):
    i=3
    i=i+1
    return HttpResponse("I am django i am a very good website development framework %s" %i)


def description_number(request, number):

    return HttpResponse("My description number is %s" % number)


def premium_members(request, number):

    try:
        query_set = Person.objects.get(pk=number)
    except Person.DoesNotExist:
        raise Http404("Person is not available")
    return render(request, 'todolist/details.html', {'query_set': query_set})
