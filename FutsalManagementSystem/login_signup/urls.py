from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('signup/',view_signup, name="signup"),
    path('login/',view_login_user, name="login"),
    path('login/logout/',view_logout, name="logout"),
    path('',get_isauthenticated_welcome, name="welcome"),
]