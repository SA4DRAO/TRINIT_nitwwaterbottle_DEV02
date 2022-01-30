from django.contrib import admin
from django.urls import path,include

from projects import views

app_name = 'projects'

urlpatterns = [
    path('' , views.index_view , name = 'home'),
    path('add_project/', views.add_project, name = 'addproject')
]
