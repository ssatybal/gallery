import profile
from django.contrib import admin
from .models import Photo, Profile, UserFavouritePhoto

# # Register your models here.
# class (admin.ModelAdmin):
#     pass

admin.site.register(Photo)
admin.site.register(Profile)
admin.site.register(UserFavouritePhoto)
