
from mimetypes import init
from urllib import request
from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    

