from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user_id = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    age = models.IntegerField()
    