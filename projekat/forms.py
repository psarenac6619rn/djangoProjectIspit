from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class DrvoForm(ModelForm):
    class Meta:
        model = Drvo
        fields = '__all__'

class StolicaForm(ModelForm):
    class Meta:
        model = Stolica
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']