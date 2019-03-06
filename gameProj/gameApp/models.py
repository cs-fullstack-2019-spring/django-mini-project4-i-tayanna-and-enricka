from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class NewgameModel(models.Model):
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    dateMade = models.DateField(default=None)
    ageLimit = models.IntegerField(default=None)
    collector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class CreateNewUserModel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirmPassword = models.CharField(max_length=200)
    dateAccountCreated = models.DateField(default=None)
    rank = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)