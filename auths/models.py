from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    U_id = models.AutoField(primary_key=True)
    U_name = models.CharField(max_length=50, blank=True, null=True)
    U_password = models.CharField(max_length=128)