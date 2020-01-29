from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', login_user, name="login_user"),
    path('login_user', login_user, name="login_user"),
    path('change_password/', change_password, name='change_password'),
    path('logout_user', logout_user, name="logout_user"),
    path('register_user', register_user, name="register_user"),
    path('index', index, name="index"),
]