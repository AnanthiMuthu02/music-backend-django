from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.get_all_artists, name='artists'),
    path('albums/', views.get_albums_with_artists, name='albums-with-artists'),
    path('songs/', views.get_songs_with_album_api, name='get_songs_with_album_api'),
    path('songs-by-album/', views.get_songs_by_album, name='get_songs_with_album_api-by-id'),
    path('albums-with-songs/', views.get_albums_with_songs_api, name='get_albums_with_songs_api'),

]