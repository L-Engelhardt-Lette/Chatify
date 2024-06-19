# models.py
from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.CharField(max_length=255)  # Changed to CharField
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}: {self.text} [{self.timestamp}]"
