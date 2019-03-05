from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def createNewUser(request):
    return HttpResponse('Creat new user page')

def loggedIn(request):
    return HttpResponse('account page when logged in')

def addGame(request):
    return HttpResponse('game form here')

