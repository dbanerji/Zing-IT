from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    numberOfSongs = models.IntegerField()

class Song(models.Model):
    track = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    playlist_id= models.IntegerField(default=0)