from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import CreateUserView

urlpatterns = [
    path('signup/',CreateUserView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name="account/login.html"),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]