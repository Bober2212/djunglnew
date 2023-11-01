from django.db import models


# Create your models here.


class Dg(models.Model):
    name = models.CharField(max_length=30)
    surnmae = models.CharField(max_length=30)
    dateofbirth = models.DateField(max_length=100)
    gmail = models.CharField(max_length=100)
    age = models.IntegerField()
    create_att = models.DateTimeField(auto_now_add=True)
    modified_att = models.DateTimeField(auto_now=True)


class Post(models.Model):
    text = models.CharField(max_length=30)
    create_att = models.DateField()
    dg = models.ForeignKey(Dg, on_delete=models.CASCADE)


class Album(models.Model):
    Album = models.CharField(max_length=30)
    Lyrics = models.DateField()  # Текст пісні
    Duration = models.CharField(max_length=30)  # Тривалість
    Rating = models.CharField(max_length=30)
    Notes = models.CharField(max_length=30)


class Musician(models.Model):
    Name = models.CharField(max_length=30)
    Instrument = models.DateField()
    Genre = models.CharField(max_length=30)
    Birthdate = models.CharField(max_length=30)
    Biography = models.CharField(max_length=30)

class I(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    gmail = models.CharField(max_length=30)
    school = models.CharField(max_length=30)


class My_school(models.Model):
    gmail_school = models.CharField(max_length=30)
    number_school = models.CharField(max_length=30)


class class_school(models.Model):
    location=models.CharField(max_length=30)
    number_school = models.CharField(max_length=30)
    number_class= models.IntegerField()
    leter_class=models.CharField(max_length=30)

class User(models.Model):
    surname = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    gmail = models.CharField(max_length=30)
    create_att = models.DateTimeField(auto_now_add=True)
    modified_att = models.DateTimeField(auto_now=True)
    date_of_birth=models.DateField()



