from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import PhotoForm

def index(request):
    infos = Profile.objects.all()
    photos = Photo.objects.select_related('user').all()
    return render(request, 'stogram/index.html', {'photos': photos, 'infos': infos})


@login_required
def account(request):

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        form.instance.user = request.user.profile
        if form.is_valid():
            form.save()
    else:
        form = PhotoForm()
    photos = Photo.objects.select_related('user').all()

    return render(request, 'stogram/account.html', {'form' : form, 'photos': photos})