from django.db import models
from django.contrib.auth.models import User as base_user


# Create your models here.


class CustomUser(base_user):
    type = models.CharField(max_length=12)


