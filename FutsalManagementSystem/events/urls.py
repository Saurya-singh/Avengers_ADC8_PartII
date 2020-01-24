from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('viewevent/',view_event_data,name='home'),
    path('eventform/',view_event_form, name='form'),
    path('eventform/save',view_event_save),
    path('viewevent/delete/<int:ID>',view_event_delete),
    path('viewevent/',get_isauthenticated_welcome),

]
