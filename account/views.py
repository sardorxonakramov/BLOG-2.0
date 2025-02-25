from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .forms import CustomUserCreationForm  
from .models import CustomUser

class CreateUserView(CreateView):
    model = CustomUser 
    form_class = CustomUserCreationForm  
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('password_change_done')


class CustomPasswordChangeDoneView(PasswordChangeView):
    template_name = 'account/password_change_done.html'
    success_url = reverse_lazy('login')