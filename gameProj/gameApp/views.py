from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    form = CreateNewUserForm(request.POST or None)
    context={

        "form":form
    }
    return render(request,'registration/login.html',context)

def logout(request):
    return render(request,'registration/logout.html')


def createNewUser(request):
    form = CreateNewUserForm(request.POST or None)
    context = {"form": form}


    if request.method == "POST":
        User.objects.create_user(request.POST['username'])
        form.save()
        return render(request, 'gameApp/loggedIn.html')

    return render(request, 'gameApp/createUser.html', context)


# @login_required
def loggedIn(request):
    allGames = NewgameModel.objects.all()
    context = {'allGames': allGames}
    return render(request, 'gameApp/loggedIn.html', context)

def addGame(request):
    form = NewGameForm(request.POST or None)
    print('gameadded')
    context = {'form': form}
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('loggedIn')
    else:
        print(form)

    return render(request, 'gameApp/addGame.html', context)



