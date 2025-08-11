from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomUserLoginForm, CustomUserEditProfileForm
from django.urls import reverse_lazy
from .models import CustomUser


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('index')

class UserLoginView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('index')

def logout_view(request):
    logout(request)
    return render(request, 'user/logout.html')


class UserProfileDetailsViews(LoginRequiredMixin, DetailView):
    model = CustomUser
    pk_url_kwarg = 'pk'
    template_name = 'user/profile_details.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['username'] = user.username
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['email'] = user.email
        context['phone_number'] = user.phone_number

        return context


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserEditProfileForm
    pk_url_kwarg = 'pk'
    template_name = 'user/profile_edit.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        return self.request.user

class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    pk_url_kwarg = 'pk'
    template_name = 'user/profile_delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user