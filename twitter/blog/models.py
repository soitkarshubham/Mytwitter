from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField(max_length = 1000)
    date_posted = models.DateTimeField(default = timezone.now)
    likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.content[:5]
