from django.urls import path, include
from . import views

# setting up path endpoints

urlpatterns = [
    path('newUser/', views.createNewUser, name='newUser'),
    path('loggedIn/', views.loggedIn, name='loggedIn'),
    path('loggedIn/addGame/', views.addGame, name='addGame'),
   ]