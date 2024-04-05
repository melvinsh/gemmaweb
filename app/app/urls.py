from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^.*$', views.catch_all, name='catch_all')
]