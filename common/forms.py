from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    number = forms.CharField()
    class Meta:
        model=User
        fields = ("username", "password1", "password2", "email","number")

