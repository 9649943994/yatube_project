from django.urls import path

from . import views

urlpatterns = [
    path('groups/<slug:slug>/', views.group_posts()),
    path('', views.index),
] 