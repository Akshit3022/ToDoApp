# This file is created by me.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('completeTask/<int:id>', views.completeTask, name='completeTask'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('logout', views.logout, name='logout'),
    path('adminDash', views.adminDash, name='adminDash'),
    path('displayTask/<int:id>', views.displayTask, name='displayTask'),
]
