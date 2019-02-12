from django.db import models


class Solo(models.Model):
    track = models.CharField(max_length=100, default='')
    artist = models.CharField(max_length=100, default='')
    instrument = models.CharField(max_length=50, default='')
    album = models.CharField(max_length=200, default='')
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
