from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']