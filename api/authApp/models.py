from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=80)