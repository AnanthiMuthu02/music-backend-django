from django.db import models
from django.conf import settings
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    upated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    short_description =models.TextField(null=True,blank=True)
    feature_img = models.FileField(upload_to='images/')
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    upated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    def get_feature_img_url(self):
        if self.feature_img:
            return settings.MEDIA_BASE_URL + self.feature_img.url
        return None
    


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name="album")
    feature_img = models.FileField(upload_to='images/',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    upated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    def get_feature_img_url(self):
        if self.feature_img:
            return settings.MEDIA_BASE_URL + self.feature_img.url
        return None