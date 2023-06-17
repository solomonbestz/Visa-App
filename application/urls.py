from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
    path('',  views.application, name='home'),
]