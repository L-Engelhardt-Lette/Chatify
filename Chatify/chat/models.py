from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}: {self.text} [{self.timestamp}]"
