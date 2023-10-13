from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

my_playlists=[
        {"id":1,"name":"Car Playlist","numberOfSongs":4},
        {"id":2,"name":"Coding Playlist","numberOfSongs":2}
    ]

def home(request):
    return render(request,'zing_it/home.html',{"my_playlist":my_playlists})


def about(request):
    return HttpResponse("""<h1>About Us:</h1><p>With Zing, you can easily find the music of your choice and easily share it with other people. You can also browse through the collections of friends, artists, and celebrities, or create a playlist of your own.
      Soundtrack your life with Zing. Subscribe or listen for free.</p>""")