from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList
# Create your views here.
def get_data(request,id):
    ls=ToDoList.objects.get(id=id)
    return HttpResponse("<h1> %s</h1>" % ls)

