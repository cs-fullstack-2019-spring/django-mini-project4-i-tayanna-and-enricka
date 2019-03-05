from django.urls import path
from . import views

# setting up path endpoints

urlpatterns = [
    path('newUser/', views.createNewUser, name='newUser'),
    path('newUser/loggedIn/<int:str>/', views.loggedIn, name='loggedIn'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/<int:str>/', views.logout, name='logout'),
    path('loggedIn/addGame/<int:str>/', views.addGame, name='addGame'),
    path('saved/', views.saveUser, name='welcome'),
    path('addGame/<int:str>', views.addGame, name='addGame')
   ]