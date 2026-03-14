"""
URL configuration for hangarin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import HomePageView, TaskList, TaskCreateView, TaskUpdateView, TaskDeleteView
from tasks.views import SubTaskList, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView
from tasks.views import CategoryList, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from tasks.views import NotesList, NotesCreateView, NotesUpdateView, NotesDeleteView
from tasks.views import PriorityList, PriorityCreateView, PriorityUpdateView, PriorityDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path('', HomePageView.as_view(), name='home'),

    # Task
    path('task_list', TaskList.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>', TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    
    # SubTask
    path('subtask_list', SubTaskList.as_view(), name = 'subtask-list'),
    path('subtask_list/add', SubTaskCreateView.as_view(), name ='subtask-add'),
    path('subtask_list/<pk>', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<pk>/delete', SubTaskDeleteView.as_view(), name='subtask-delete'),
    
    #Category
    path('category_list', CategoryList.as_view(), name = 'category-list'),
    path('category_list/add', CategoryCreateView.as_view(), name = 'category-add'),
    path('category_list/<pk>', CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    
    # Notes
    path('notes_list', NotesList.as_view(), name = 'notes-list'),
    path('notes_list/add', NotesCreateView.as_view(), name = 'notes-add'),
    path('notes_list/<pk>', NotesUpdateView.as_view(), name='notes-update'),
    path('notes_list/<pk>/delete', NotesDeleteView.as_view(), name='notes-delete'),
   
    # Priority
    path('priority_list', PriorityList.as_view(), name = 'priority-list'),
    path('priority_list/add', PriorityCreateView.as_view(), name = 'priority-add'),
    path('priority_list/<pk>', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'),
   
]