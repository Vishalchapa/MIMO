from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.views.generic import UpdateView, DeleteView


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

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('dashboard')
   
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
  
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)