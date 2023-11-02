from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Form(forms.Form):
    surname=forms.CharField()
    phone_number=forms.IntegerField()
    gmail=forms.CharField()

class Registration(forms.Form):
    surname=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    phone_number=forms.IntegerField()
    gmail=forms.CharField()
    data=forms.DateField(widget=forms.SelectDateWidget())

class Login(forms.Form):
    surname=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    phone_number=forms.IntegerField()
    gmail=forms.CharField()


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']


