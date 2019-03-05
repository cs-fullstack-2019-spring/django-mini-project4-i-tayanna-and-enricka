from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
# this function will take you to the home page of the website.
def index(request):
    return  render(request,"gameApp/index.html")

def newuser(request):

