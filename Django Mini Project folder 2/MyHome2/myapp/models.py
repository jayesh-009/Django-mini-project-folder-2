from django.db import models


# Create your models here.
class Employee(models.Model):

    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=30)

class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()
    


class Movie(models.Model):

    rdate=models.CharField(max_length=30)
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()

class Login(models.Model):

    name=models.CharField(max_length=30)
    datetime=models.CharField(max_length=30)

class Additem(models.Model):

    name=models.CharField(max_length=30)
    quantity=models.IntegerField()





