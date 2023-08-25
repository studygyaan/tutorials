# tasks/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

def tasks(request):
    return render(request, 'tasks.html')

def get_tasks(request):
    tasks = Task.objects.all()
    task_list = [{'title': task.title} for task in tasks]
    return JsonResponse(task_list, safe=False)

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task.objects.create(title=title)
        return JsonResponse({'status': 'success'})
