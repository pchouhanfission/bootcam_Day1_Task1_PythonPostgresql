from django.db import models

# Create your models here.
class Info(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    citizen = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
