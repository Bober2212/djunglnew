from django import forms



class Form(forms.Form):
    surname=forms.CharField()
    phone_number=forms.IntegerField()
    gmail=forms.CharField()
    photo=forms.FileField()