from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    tasks=Task.objects.order_by("-id")
    return render(request,'main/index.html', {'title':"Введіть ім'я"})


def create(request):
    tasks = Task.objects.order_by("-id")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    form=TaskForm()
    context={
             'form': form,
             'tasks': tasks
    }
    return render(request,'main/create.html',context)