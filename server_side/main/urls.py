from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views
urlpatterns = [
    path('test/', lambda req: render(req, "test.html")),
    path('post_msg/', views.post_message),
    path('register/', views.register),
    path('post/', views.post),
    path('fetch_posts/', views.fetch_posts),
    path('post_detail/', views.get_post_detail),
    path('create_team/', views.create_team),
    path('fetch_teams/', views.fetch_teams),
    path('team_detail/', views.get_team_detail),
]