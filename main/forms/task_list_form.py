from django import forms
from main.models import TaskList, Organization


class TaskListForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control mb-3'})
    )
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control mb-3 disabled'})
    )

    class Meta:
        model = TaskList
        fields = ('title', 'organization')