# Generated by Django 4.0.2 on 2022-03-10 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stogram', '0003_userfavouritephoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfavouritephoto',
            old_name='photo',
            new_name='favourite_photo',
        ),
    ]