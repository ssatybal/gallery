from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import PhotoForm
from django.db.models import Prefetch

def index(request):
    photos = Photo.objects.select_related('user').prefetch_related(
        Prefetch('favourite_photo', UserFavouritePhoto.objects.filter(user=request.user if not request.user.is_anonymous else None), to_attr="already_favourite"))
    return render(request, 'stogram/index.html', {'photos': photos, 'is_user_anonymous': request.user.is_anonymous})


def toggle_favourite(request, photo_id):
    exists_model = UserFavouritePhoto.objects.filter(user=request.user, photo=photo_id)

    if exists_model:
        exists_model.delete()
        return redirect('index_url')

    photo = Photo.objects.get(id=photo_id)
    new = UserFavouritePhoto()
    new.user = request.user
    new.photo = photo
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
    favourite_photos = UserFavouritePhoto.objects.filter(user=request.user).select_related('photo')

    return render(request, 'stogram/account.html', {'form' : form, 'photos': photos, 'favourite_photos': favourite_photos})


def delete_photo(request, photo_id):
    data = Photo.objects.get(id=photo_id)
    data.delete()
    return redirect('index_url')

