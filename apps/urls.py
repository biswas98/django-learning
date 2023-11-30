from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path('', views.index, name='home'),
    path('chatBot_openAI/', views.chatBot_openAI, name='chatBot_openAI'),

]
