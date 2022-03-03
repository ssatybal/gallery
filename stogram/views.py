from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect

@login_required
def index(request):
    return render(request, 'stogram/index.html')


def view_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PhotoForm()
        photos = Photo.objects.all()
    return render(request, 'stogram/view_photo.html', {'form' : form, 'photos': photos})
  
  
def success(request):
    return HttpResponse('successfully uploaded')    
