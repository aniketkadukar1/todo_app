from django.shortcuts import render, redirect
from .models import Task
from .forms import AddTaskForm

# Create your views here.
def index(request):
    task_list = Task.objects.all()
    task_count = Task.objects.count()
    context = {'task_list': task_list, 'task_count': task_count}
    return render(request, 'todo/index.html', context=context)

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    form = AddTaskForm()
    context = {'form': form}
    return render(request, 'todo/add_task.html', context=context)