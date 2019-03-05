from django.shortcuts import render

from django .http import HttpResponse

# Create your views here.
# this function will take you to the home page of the website.
def index(request):
    return  render(request,"gameApp/index.html")

def newuser(request):




def createNewUser(request):
    return HttpResponse('Creat new user page')

def loggedIn(request):
    return HttpResponse('account page when logged in')

def addGame(request):
    return HttpResponse('game form here')


