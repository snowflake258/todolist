from django import forms
from main.models import Task, TaskList


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control mb-3'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={ 'class': 'form-control mb-3'})
    )
    task_list = forms.ModelChoiceField(
        queryset=TaskList.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-3 disabled'})
    )

    class Meta:
        model = Task
        fields = ('name', 'description', 'task_list')