from django.urls import path
from django.contrib import admin
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('Register_BusinessOwner/', views.register, name='Register_BusinessOwner'),
    path('login_businessowner/', views.login_businessowner, name='Login_BusinessOwner'),
    path('logout_businessowner/', auth_views.LoginView.as_view(template_name='Logout_BusinessOwner.html'), name='Logout_BusinessOwner'),
    path('profile_businessOwner/', views.profile, name = 'profile_businessOwner'),

]