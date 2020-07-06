import django.forms as forms
from main.models import Organization


class LoginForm(forms.Form):
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'value': 'sergey.semyonov.258@gmail.com'})
    )
    password = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'value': 'qdg058znm230'})
    )
    organization = forms.ChoiceField(
        choices=((1, 'Microsoft'), (2, 'IBM'), (3, 'Google')),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control mb-3'})
    )