from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.


def home(req):
    # return HttpResponse("hello from todo")
    taskData = Task.objects.all()
    print(taskData)
    context = {"object": taskData}
    return render(req, "home.html", context)


def detailView(req, pk):
    todo = get_object_or_404(Task, pk=pk)
    context = {"todo": todo, "pk": pk}
    return render(req, "todo.html", context)
