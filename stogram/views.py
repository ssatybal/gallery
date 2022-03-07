from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import PhotoForm

def index(request):
    photos = Photo.objects.all()
    return render(request, 'stogram/index.html', {'photos': photos})


@login_required
def account(request):

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        form.instance.user = request.user.profile
        if form.is_valid():
            form.save()
    else:
        form = PhotoForm()
    photos = Photo.objects.all()

    return render(request, 'stogram/account.html', {'form' : form, 'photos': photos})    

