from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

def tasks(request):
    return render(request, 'tasks.html')

def get_tasks(request):
    tasks = Task.objects.all()
    task_list = [{'id': task.id, 'title': task.title, 'completed': task.completed} for task in tasks]
    return JsonResponse(task_list, safe=False)

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        task = Task.objects.create(title=title)
        return JsonResponse({'status': 'success'})

def update_task_status(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        completed = request.POST.get('completed')
        if completed == 'true':
            completed = True
        else:
            completed = False
        task = Task.objects.get(id=id)
        task.completed = completed
        task.save()  # Save the changes to the task
        return JsonResponse({'status': 'success'})

def delete_task(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'status': 'success'})