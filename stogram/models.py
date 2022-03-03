from django.db import models
# forms.py
from django import forms
from .models import *


class Photo(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'photo'



class PhotoForm(forms.ModelForm):

	class Meta:
		model = Photo
		fields = ['path', 'description']
