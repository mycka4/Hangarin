from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task, SubTask, Category, Note, Priority
from tasks.forms import TaskForm, SubTaskForm, CategoryForm, NotesForm, PriorityForm

class HomePageView(LoginRequiredMixin,  ListView):
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

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(title__icontains=query)

        status = self.request.GET.get('status', '')
        if status:
            queryset = queryset.filter(status=status)
        
        priority = self.request.GET.get('priority', '')
        if priority:
            queryset = queryset.filter(priority__name=priority)

        category = self.request.GET.get('category', '')
        if category:
            queryset = queryset.filter(category__name=category)
        
        sort = self.request.GET.get('sort', '-created_at')
        valid_sorts = ['title', '-title', 'deadline', '-deadline', 'status', '-status', 'created_at', '-created_at']
        if sort in valid_sorts:
            queryset = queryset.order_by(sort)
 
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['selected_status'] = self.request.GET.get('status', '')
        context['selected_priority'] = self.request.GET.get('priority', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_sort'] = self.request.GET.get('sort', '-created_at')
        context['priorities'] = Priority.objects.all()
        context['categories'] = Category.objects.all()
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

class SubTaskList(LoginRequiredMixin, ListView):
    model = SubTask 
    context_object_name = 'subtasks'
    template_name = 'subtask_list.html'
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(title__icontains=query)

        status = self.request.GET.get('status', '')
        if status:
            queryset = queryset.filter(status=status)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        context['selected_status'] = self.request.GET.get('status', '')
        return context
    

class SubTaskCreateView(LoginRequiredMixin, CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(LoginRequiredMixin, UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(LoginRequiredMixin, DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_list.html'
    paginate_by = 5
    ordering = ['-created_at']

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model =  Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model =  Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

class NotesList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes_list.html'
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
 
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(content__icontains=query)
 
        created_at = self.request.GET.get('created_at', '')
        if created_at:
            queryset = queryset.filter(created_at__date=created_at)
 
 
        return queryset

class NotesCreateView(LoginRequiredMixin, CreateView):
    model =  Note
    form_class = NotesForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('notes-list')

class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model =  Note
    form_class = NotesForm
    template_name = 'notes_form.html'
    success_url = reverse_lazy('notes-list')

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes_del.html'
    success_url = reverse_lazy('notes-list')

class PriorityList(LoginRequiredMixin, ListView):
    model = Priority
    context_object_name = 'priorities'
    template_name = 'priority_list.html'
    paginate_by = 5
    ordering = ['-created_at']

class PriorityCreateView(LoginRequiredMixin, CreateView):
    model =  Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(LoginRequiredMixin, UpdateView):
    model =  Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(LoginRequiredMixin, DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

