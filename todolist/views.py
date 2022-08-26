from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("Django!")

def description(request):
    i=5
    i=i+1
    return HttpResponse("I am django i am a very good website development framework %s" %i)


def description_number(request, number):

    return HttpResponse("My description number is %s" % number)





