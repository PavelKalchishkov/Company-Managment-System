from django.contrib.auth import logout
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.urls import reverse_lazy


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
