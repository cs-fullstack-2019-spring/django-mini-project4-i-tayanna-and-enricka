from django.urls import path
from . import views

# setting up path endpoints

urlpatterns = [
    path('newUser/', views.createNewUser, name='newUser'),
    path('newUser/loggedIn/', views.loggedIn, name='loggedIn'),
    path('loggedIn/addGame/', views.addGame, name='addGame'),
    path('saved/', views.saveUser, name='welcome')
   ]