from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.models import User
from users.forms import UserLoginForm, UserRegistationForm, UserProfileForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixixn


class UserLoginView(TitleMixixn, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Login'

class UserRegistrationView(SuccessMessageMixin, TitleMixixn, CreateView):
    model = User
    form_class = UserRegistationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Registration'

class UserProfileView(LoginRequiredMixin, TitleMixixn, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Profile'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

    def get_object(self, queryset=None):
        return self.request.user
