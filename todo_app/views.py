from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def task_list(request):
    if request.user.is_authenticated:
        tasks = request.user.tasks.all()
        return render(request, 'todo_app/task_list.html', {'all_tasks': tasks})
    else:
        return render(request, 'todo_app/home.html', {})

def new_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return render(request, 'todo_app/task_detail.html', {'task': task})
    else:
        return render(request, 'todo_app/task_form.html', {'form': form, 'new_or_edit': 'New'})

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'todo_app/task_detail.html', {'task': task})

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return render(request, 'todo_app/task_detail.html', {'task': task})
    else:
        form = TaskForm(instance=task)
        return render(request, 'todo_app/task_form.html', {'form': form, 'new_or_edit': 'Edit'})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo:task_list')
