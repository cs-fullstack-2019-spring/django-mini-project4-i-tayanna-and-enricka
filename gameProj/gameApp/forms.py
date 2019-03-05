from django import forms
from .models import NewgameModel, CreateNewUserModel



class NewGameForm(forms.ModelForm):
    class Meta:
        exclude = ['collector']
        model = NewgameModel


class CreateNewUserForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = CreateNewUserModel