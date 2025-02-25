from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm  # <-- TO'G'RI FORMNI IMPORT QILAMIZ
from .models import CustomUser

class CreateUserView(CreateView):
    model = CustomUser  # <-- Modelni ham kiritamiz
    form_class = CustomUserCreationForm  # <-- `UserCreationForm` o'rniga `CustomUserCreationForm`
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'
