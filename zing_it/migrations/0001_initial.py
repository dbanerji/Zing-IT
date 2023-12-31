# Generated by Django 4.2.6 on 2023-11-08 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('numberOfSongs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('track', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255, unique=True)),
                ('album', models.CharField(max_length=255)),
                ('length', models.CharField(max_length=255)),
                ('playlist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zing_it.playlist')),
            ],
        ),
    ]
