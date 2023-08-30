from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import MyModelForm

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


def create_todo(req):
    if req.method == "POST":
        form = MyModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("/todo")
    else:
        form = MyModelForm()

    return render(req, "create.html", {"form": form})


def update_todo(req, pk):
    todo = get_object_or_404(Task, pk=pk)
    if req.method == "POST":
        form = MyModelForm(req.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("/todo")
    else:
        form = MyModelForm(instance=todo)

    context = {"form": form, "todo": todo}
    return render(req, "update.html", context)


def delete_todo(req, pk):
    todo = get_object_or_404(Task, pk=pk)
    todo.delete()
    return redirect("/todo")
