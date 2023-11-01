from django import forms



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



