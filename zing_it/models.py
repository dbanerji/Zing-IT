from django.db import models

# Create your models here.
class Playlist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique= True,max_length=255)
    numberOfSongs = models.IntegerField()

class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    track = models.CharField(max_length=255)
    artist = models.CharField(unique= True,max_length=255)
    album = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    playlist_name= models.ManyToManyField('Playlist')