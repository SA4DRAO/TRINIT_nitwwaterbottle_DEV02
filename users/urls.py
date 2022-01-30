from django.contrib import admin
from django.urls import path,include

from users import views

app_name = 'users'

urlpatterns = [
    path('login/' , views.login_view , name ='login'),
    path("logout/", views.logout_view, name='logout'),
    path('register/' , views.register_view , name ='register'),
    path('<str:username>/' , views.profile_view , name ='profile')
]
