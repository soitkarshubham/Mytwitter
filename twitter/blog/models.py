from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField(max_length = 1000)
    date_posted = models.DateTimeField(default = timezone.now)
    date_updated = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-date_posted']


    def __str__(self):
        return self.content[:5]
