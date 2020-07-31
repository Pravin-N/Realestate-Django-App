from django.urls import path #step 32.8

from . import views #step 32.8

urlpatterns = [
    path('login', views.login, name='login'), #step 32.8
    path('register', views.register, name='register'), #step 32.8
    path('logout', views.logout, name='logout'), #step 32.8
    path('dashboard', views.dashboard, name='dashboard'), #step 32.8
    ]
