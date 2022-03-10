from pyexpat import model
from django.db import models
# forms.py
from django import forms
from .models import *
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/')


class Photo(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_photo', null=True)

    class Meta:
        db_table = 'photo'


class UserFavouritePhoto(models.Model):
    favourite_photo_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_photo_user')
    favourite_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='favourite_photo')

    class Meta:
        db_table = 'favourite'