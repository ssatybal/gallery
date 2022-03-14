from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('account', views.account, name='account_url'),
    path('toggle_favourite/<int:photo_id>', views.toggle_favourite, name='toggle_favourite_url'),
    path('delete_photo/<int:photo_id>', views.delete_photo, name='delete_photo_url')
]