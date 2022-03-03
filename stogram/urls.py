from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index),
    path('view_photo', views.view_photo, name='view_photo_url'),
    path('success', views.success, name='success')
]