from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import Links, Videos


class User(AbstractUser):
    favorite_links = models.ManyToManyField(Links, blank=True)
    favorite_videos = models.ManyToManyField(Videos, blank=True)
