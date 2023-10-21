from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views
urlpatterns = [
    path('test/', lambda req: render(req, "test.html")),
    path('post/', views.post_message),
    path('register/', views.register)
]