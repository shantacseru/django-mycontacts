from django.shortcuts import render, redirect
from .models import Contacts
from .forms import ContactForm, SignUpForm
import logging
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound


logger = logging.getLogger(__name__)


def signup(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'form.html', {'form': form, 'title': 'Sign Up', 'browserTabTitle': 'Signup',
                                         'submit': 'Sign Up', 'authText': 'Login', 'authLink': '/accounts/login'})


@login_required(login_url='/accounts/login')
def dashboard(request):
    username = request.user.username
    if Contacts.objects.filter(user_id=username).exists():
        contacts = Contacts.objects.filter(user_id=username)
        return render(request, 'dashboard.html', {'contacts': contacts, 'authText': 'Logout',
                                                  'authLink': '/accounts/logout'})
    else:
        return render(request, 'dashboard.html', {'contacts': [], 'authText': 'Logout', 'authLink': '/accounts/logout'})


@login_required(login_url='/accounts/login')
def addcontact(request):
    form = ContactForm(request.POST or None)
    username = request.user.username
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user_id = username
        obj.save()
        return redirect('allcontacts')
    else:
        return render(request, 'form.html', {'form': form, 'title': 'Add New Contact', 'browserTabTitle': 'Add Contact',
                                             'submit': 'Add', 'authText': 'Logout', 'authLink': '/accounts/logout'})


def notfound(request, param):
    if not param:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

    return render('404.html', {'authText': 'Login', 'authLink': '/accounts/login'})

