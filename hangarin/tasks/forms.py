from django.forms import ModelForm
from django import forms
from .models import Task, SubTask

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'
                },
                format='%Y-%m-%dT%H:%M'
            ),
        }

class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = "__all__"