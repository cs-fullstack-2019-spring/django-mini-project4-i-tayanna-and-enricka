from django.shortcuts import render
from .forms import CreateNewUserForm, NewGameForm
from .models import NewgameModel, CreateNewUserModel
from .forms import CreateNewUserForm

from django .http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.
# this function will take you to the home page of the website.
def index(request):
    return render(request,"gameApp/index.html")

def login(request):
    form=CreateNewUserForm(request.POST or None)
    context={

        "form":form
    }
    return render(request,'registeration/login.html',context)


def logout(request):
    return render(request,'registeration/logout.html')

def createNewUser(request):
    form = CreateNewUserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'gameApp/createUser.html', context)

def saveUser(request):
    form = CreateNewUserForm(request.POST or None)
    if request.method == "POST":
        User.objects.create_user(request.POST['username'])
        form.save()
        return render(request, 'gameApp/loggedIn.html')



def loggedIn(request):
    return render(request, 'gameApp/loggedIn.html')

def addGame(request):
    form = NewGameForm(request.POST or None)
    context = {'form': form}
    return render(request, 'gameApp/addGame.html', context)


