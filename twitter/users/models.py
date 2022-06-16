from django.db import models
from django.contrib.auth.models import User
#from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, blank=True ,null=True, on_delete=models.CASCADE)
    image = models.ImageField(default ='default.png',blank = True, null = True)
    bio = models.TextField(default = '')

    def __str__(self):
        return f'{self.user.username}'