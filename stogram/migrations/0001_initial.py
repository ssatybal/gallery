# Generated by Django 4.0.2 on 2022-03-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('path', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]