from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe


# Create your models here.

class Banners(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))


class Photo(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return "photos/{0}".format(self.user.username)
        return None

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="photos", verbose_name="Photo")
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Désignation")

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    logo = models.FileField(null=True, blank=True, default="logos/album.jpeg", upload_to="logo")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def nb_photos(self):
        nb = self.albumdetail_set.count()
        if nb is None:
            return 0
        else:
            return nb
        # return self.albumdetail_set.count() 


class AlbumDetail(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
