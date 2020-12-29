from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=124)
    phone = models.CharField(max_length=14)
    feedback = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Buy_Model(models.Model):
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)















