from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import PhotoForm

def index(request):
    photos = Photo.objects.select_related('user').all()
    return render(request, 'stogram/index.html', {'photos': photos})


def toggle_favourite(request, photo_id):
    exists_model = UserFavouritePhoto.objects.filter(favourite_photo_user=request.user, favourite_photo=photo_id)

    if exists_model:
        exists_model.delete()
        return redirect('index_url')

    photo = Photo.objects.get(id=photo_id)
    new = UserFavouritePhoto()
    new.favourite_photo_user = request.user
    new.favourite_photo = photo
    new.save()
    return redirect('index_url')


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
    favourite_photos = Photo.objects.filter(id__in=UserFavouritePhoto.objects.filter(favourite_photo_user=request.user))

    return render(request, 'stogram/account.html', {'form' : form, 'photos': photos, 'favorite_photos': favourite_photos})