from re import search
from django.contrib import admin
from django.urls import path
from contact import views


app_name = 'contact'

urlpatterns = [
    path('', views.index, name="index"),
    path('users-json/', views.users_json, name='users'),
    path('<int:id>/', views.user_detail, name='user'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create')
    
]