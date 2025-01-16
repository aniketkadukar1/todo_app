from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    task_list = Task.objects.all()
    task_count = Task.objects.count()
    context = {'task_list': task_list, 'task_count': task_count}
    return render(request, 'todo/index.html', context=context)