from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


def get_coins():
    return 100


class CustomUser(AbstractUser):
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    coins = models.IntegerField(default=get_coins())

    def __str__(self):
        return self.name