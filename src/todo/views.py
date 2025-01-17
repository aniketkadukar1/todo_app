from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import AddTaskForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_tasks = Task.objects.all()
    paginator = Paginator(all_tasks, 5)
    page_number = request.GET.get("page")
    task_list = paginator.get_page(page_number)
    
    task_count = Task.objects.count()
    context = {'task_list': task_list, 'task_count': task_count}
    return render(request, 'todo/index.html', context=context)

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
        # Don't overwrite the form if it's invalid
        return render(request, 'todo/add_task.html', {'form': form})

    # Render an empty form for GET requests
    form = AddTaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    form = AddTaskForm(instance= task)
    if request.method == "POST":
        form = AddTaskForm(request.POST, instance= form)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    return render(request, 'todo/edit_task.html', {'form' : form})

def delete_task(request, task_id):
    task = Task.objects.get(pk = task_id)
    task.delete()
    return redirect('todo:index')

def mark_completed(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        is_completed = request.POST.get("is_completed") == "true"
        task.is_completed = is_completed
        task.save()
    return redirect("todo:index")


        