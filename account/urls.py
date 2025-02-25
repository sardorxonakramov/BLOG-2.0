from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import CreateUserView, CustomPasswordChangeDoneView, CustomPasswordChangeView

urlpatterns = [
    path('signup/',CreateUserView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name="account/login.html"),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('password_change/',CustomPasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',CustomPasswordChangeDoneView.as_view(),name='password_change_done'),
]