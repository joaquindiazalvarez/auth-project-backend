from django.db import models

class User(models.Model):
    """
    Model for store user data
    """
    name = models.CharField(max_length=120, null=False)
    email = models.CharField(max_length=120, unique=True, null=False)
    password = models.CharField(max_length=80, null=False)
    birthdate = models.DateField(null=False)