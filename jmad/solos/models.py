from django.db import models


class Solo(models.Model):
    track = models.CharField(max_length=100, default='')
    artist = models.CharField(max_length=100, default='')
    instrument = models.CharField(max_length=50, default='')
