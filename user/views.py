from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)


def login(request):
    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(request, data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponse('KASHFKJHASLFH')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'user/login.html', context)