import email
from tokenize import group
from django.db import models
from django.urls import reverse
from datetime import date, datetime
# Import the User
from django.contrib.auth.models import User

class Group(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    leader = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('index')


class Event(models.Model):
    title = models.CharField(max_length=100)
    host = models.CharField(max_length=100) # potential to change to dropdown(Group Members)
    location = models.CharField(max_length=100)
    datetime = models.DateTimeField()

    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group}'s event on {self.datetime}"

class Profile(models.Model):
    name = models.CharField(max_length=50)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.name }'

    # leader_username = models.CharField(max_length=50)
    # members = models.ManyToManyField(User)