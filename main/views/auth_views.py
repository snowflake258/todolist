from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as django_authenticate, login as django_login, logout as django_logout
from main.forms import LoginForm
from main.models import Organization


def login_view(request):
    print(request.session.get('org_id'))

    if request.method != 'POST':
        return render(request, 'main/login.html', {'form': LoginForm()})

    form = LoginForm(request.POST)
    if form.is_valid():
        return login_execute(request, form)
    else:
        return render(request, 'main/login.html', {'form': form})


def login_execute(request, form: LoginForm):
    user = User.objects.filter(email=form.cleaned_data['email']).first()
    
    if user == None:
        form.add_error('email', 'Incorrect email.')
        return render(request, 'main/login.html', {'form': form})
    
    if not user.organization_set.filter(id=form.cleaned_data['organization']).exists():
        form.add_error('organization', 'This user have not access to this organization.')
        return render(request, 'main/login.html', {'form': form})
  
    user = django_authenticate(username=user.username, password=form.cleaned_data['password'])
    if user is None:
        form.add_error('password', 'Incorrect password.')
        return render(request, 'main/login.html', {'form': form})
    else:
        django_login(request, user)
        organization = Organization.objects.get(id=form.cleaned_data['organization'])
        request.session['org_id'] = organization.id
        request.session['org_name'] = organization.name
        

    return HttpResponseRedirect(reverse('main:task_lists'))


def logout_view(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('main:login'))
