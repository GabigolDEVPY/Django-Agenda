from django.contrib import admin
from django.urls import path
from contact import views
import contact

app_name = 'contact'

urlpatterns = [
    path('', views.index, name="index"),
    path('users-json/', lambda request: views.Users().users_view(request), name='users'),
    path('<int:id>/', lambda request, id: views.Users(id).user_view(request), name='user')
]