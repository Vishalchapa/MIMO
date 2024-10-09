from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
def dashboard(request):
    # Get active and completed tasks for the user
    active_tasks = Task.objects.filter(user=request.user, status__in=[0, 1])  # 0: Not Started, 1: In Progress
    completed_tasks = Task.objects.filter(user=request.user, status=2)  # 2: Completed
    # This handles task creation
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign task to logged-in user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    # This handles search query
    query = request.GET.get('q')
    if query:
        search_results = Task.objects.filter(user=request.user, title__icontains=query)
    else:
        search_results = None  # No search performed
    context = {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
        'form': form,
        'search_results': search_results,
        'query': query
    }
    return render(request, 'tasks/dashboard.html', context)