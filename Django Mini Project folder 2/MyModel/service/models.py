from django.db import models

# Create your models here.
class Stud(models.Model):
	name=models.CharField(max_length=100)
	city=models.CharField(max_length=100)

class Emp(models.Model):
	name=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
