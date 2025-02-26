from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import CreateUserView, CustomPasswordChangeDoneView, CustomPasswordChangeView

urlpatterns = [
    path('signup/',CreateUserView.as_view(),name='signup'),
    path('login/',LoginView.as_view(template_name="account/login.html"),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('password_change/',CustomPasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',CustomPasswordChangeDoneView.as_view(),name='password_change_done'),

    # password_reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/register/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='account/register/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/register/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/register/password_reset_complete.html'), name='password_reset_complete'),
  


]