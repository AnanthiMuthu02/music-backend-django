from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist, Album, Song
# Create your views here.




def get_all_artists(request):
    artists = Artist.objects.filter(is_active=True)
    data = [{'id': artist.id, 'name': artist.name,'img':artist.get_img_url()} for artist in artists]
    return JsonResponse(data, safe=False)


def get_albums_with_artists(request):
    albums = Album.objects.all()
    serialized_data = [serialize_album_with_artist(album) for album in albums]
    return JsonResponse(serialized_data, safe=False)

def serialize_album_with_artist(album):
    return {
        'id': album.id,
        'title': album.title,
        'feature_img': album.get_feature_img_url(), 
        'short_description': album.short_description,
        'artist': {
            'id': album.artist.id,
            'name': album.artist.name
        }
    }


def get_songs_with_album_api(request):
    songs = Song.objects.select_related('album').filter(is_active=True)

    # Prepare JSON data to return
    songs_data = []
    for song in songs:
        song_data = {
            'id': song.id,
            'title': song.title,
            'feature_img': song.feature_img.url if song.feature_img else None,
            'album': {
                'id': song.album.id,
                'title': song.album.title,
                'artist': song.album.artist.name if song.album.artist else None,
                'feature_img': song.album.get_feature_img_url(), 
            },
            'created_at': song.created_at,
            'updated_at': song.upated_at
        }
        songs_data.append(song_data)

    return JsonResponse(songs_data, safe=False)


def get_albums_with_songs_api(request):
    albums = Album.objects.all()

    # Prepare JSON data to return
    albums_data = []
    for album in albums:
        album_data = {
            'album_title': album.title,
            'artist': album.artist.name if album.artist else None,
            'feature_img': album.get_feature_img_url(), 
            'songs': []
        }
        # Retrieve songs associated with the current album
        songs = Song.objects.filter(album=album).all() 
        for song in songs:
            song_data = {
                'title': song.title,
                'feature_img': song.get_feature_img_url(),
               
            }
            album_data['songs'].append(song_data)
        
        albums_data.append(album_data)
    return JsonResponse(albums_data, safe=False)



def get_songs_by_album(request):

    id = request.GET.get("id")
    if id is None:
        return JsonResponse({"message":"id is not defined"})
    songs = Song.objects.filter(album_id=id).select_related('album').filter(is_active=True)

    # Prepare JSON data to return
    songs_data = []
    for song in songs:
        song_data = {
            'id': song.id,
            'title': song.title,
            'feature_img': song.feature_img.url if song.feature_img else None,
            'album': {
                'id': song.album.id,
                'title': song.album.title,
                'artist': song.album.artist.name if song.album.artist else None,
                'feature_img': song.album.get_feature_img_url(), 
            },
            'created_at': song.created_at,
            'updated_at': song.upated_at
        }
        songs_data.append(song_data)

    return JsonResponse(songs_data, safe=False)