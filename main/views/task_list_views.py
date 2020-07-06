from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from main.models import Organization, TaskList
from main.forms import TaskListForm


class TaskListsView(ListView):
    template_name = 'main/task_lists.html'
    context_object_name = 'task_lists'

    def get_queryset(self):
        org_id = self.request.session.get('org_id')
        organization = Organization.objects.get(id=org_id)
        return TaskList.objects.filter(organization=organization)


class TaskListCreateView(CreateView):
    template_name = 'main/task_list_create.html'
    form_class = TaskListForm
    success_url = reverse_lazy('main:task_lists')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['organization'].queryset = Organization.objects.filter(id=self.request.session.get('org_id'))
        return form


class TaskListUpdateView(UpdateView):
    template_name = 'main/task_list_update.html'
    model = TaskList
    form_class = TaskListForm
    success_url = reverse_lazy('main:task_lists')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['organization'].queryset = Organization.objects.filter(id=self.request.session.get('org_id'))
        return form


class TaskListDeleteView(DeleteView):
    template_name = 'main/task_list_delete.html'
    model = TaskList
    success_url = reverse_lazy('main:task_lists')
