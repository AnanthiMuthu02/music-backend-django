from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Artist)
class AdminArtist(admin.ModelAdmin):
    list_display=["name","is_active","created_at"]
    search_fields=["name"]
    list_filter =["name","created_at"]

@admin.register(models.Album)
class AdminAlbum(admin.ModelAdmin):
    list_display=["title","artist","is_active","created_at"]
    search_fields=["title"]
    list_filter =["title","created_at"]

@admin.register(models.Song)
class AdminSong(admin.ModelAdmin):
    list_display=["title","album","is_active","created_at"]
    search_fields=["title"]
    list_filter =["title","created_at"]