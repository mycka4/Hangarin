from django.shortcuts import render
from django.views.generic.list import ListView
from tasks.models import Task

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tasks'] = Task.objects.count()
        context['completed_tasks'] = Task.objects.filter(status='Completed').count()
        context['inprogress_tasks'] = Task.objects.filter(status='In Progress').count()
        context['pending_tasks'] = Task.objects.filter(status='Pending').count()
        return context

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'
    paginate_by = 5


