from django.contrib import admin
from .models import CreateNewUserModel, NewgameModel
# Register your models here.

admin.site.register(CreateNewUserModel)
admin.site.register(NewgameModel)