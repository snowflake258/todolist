from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.models import Task, TaskList, Organization
from main.forms import TaskForm


class TasksView(ListView):
    template_name = 'main/tasks.html'
    context_object_name = 'tasks'


    def get_queryset(self):
        task_list = TaskList.objects.get(pk=self.kwargs['task_list_id'])
        return Task.objects.filter(task_list=task_list)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['task_list_id'] = self.kwargs['task_list_id']
        context['task_list_name'] = TaskList.objects.get(id=self.kwargs['task_list_id']).title
        return context


class TaskCreateView(CreateView):
    template_name = 'main/task_create.html'
    form_class = TaskForm


    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        organization = Organization.objects.get(id=self.request.session.get('org_id'))
        form.fields['task_list'].queryset = TaskList.objects.filter(organization=organization)
        return form

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['task_list_id'] = self.kwargs['task_list_id']
        return context


    def get_success_url(self):
        return reverse_lazy('main:tasks', kwargs={ 'task_list_id': self.kwargs['task_list_id'] })


class TaskUpdateView(UpdateView):
    template_name = 'main/task_update.html'
    model = Task
    form_class = TaskForm


    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        organization = Organization.objects.get(id=self.request.session.get('org_id'))
        form.fields['task_list'].queryset = TaskList.objects.filter(organization=organization)
        return form
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['task_list_id'] = self.kwargs['task_list_id']
        return context


    def get_success_url(self):
        return reverse_lazy('main:tasks', kwargs={ 'task_list_id': self.kwargs['task_list_id'] })


class TaskDeleteView(DeleteView):
    template_name = 'main/task_delete.html'
    model = Task
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['task_list_id'] = self.kwargs['task_list_id']
        return context


    def get_success_url(self):
        return reverse_lazy('main:tasks', kwargs={ 'task_list_id': self.kwargs['task_list_id'] })