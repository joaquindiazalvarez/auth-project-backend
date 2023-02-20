from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, unique = True)
    password = models.CharField(max_length=80)
    birthdate = models.DateField(null=True)