from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.models import User
from users.forms import UserLoginForm, UserRegistationForm, UserProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from products.models import Basket

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    data = {
        'title': 'Вход на сайт',
        'form': form,
    }
    return render(request, 'users/login.html', data)

def register(request):
    if request.method == 'POST':
        form = UserRegistationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistationForm()

    data = {
        'title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', data)
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance= request.user, data=request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    basket = Basket.objects.filter(user = request.user)
    data = {
        'title': 'Профиль',
        'form': form,
        'baskets': basket,
    }
    return render(request, 'users/profile.html', data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

