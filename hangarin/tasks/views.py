from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tasks.models import Task, SubTask, Note, Category, Priority
from tasks.form import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm
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

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')
