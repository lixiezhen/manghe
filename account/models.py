from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return "user:{}".format(self.user.username)