from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class Maps(models.Model):
    """Model representing map."""
    name = models.CharField(
        max_length=200, help_text='Enter a map (e.g. Inferno)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Videos(models.Model):
    title = models.CharField(max_length=200)

    link = models.TextField(max_length=1000, help_text='Enter the link')
    map_belong = models.ForeignKey('Maps', on_delete=models.SET_NULL, null=True)
    SITE = (
        ('a', 'A'),
        ('b', 'B'),
        ('mid', 'Middle'),
    )
    TYPE = (
        ('Smoke', 'smoke'),
        ('Molly', 'molly'),
        ('Flash', 'flash')
    )
    type_video = models.CharField(
        max_length=6,
        choices=TYPE,
        blank=True,
        help_text='Pick a type',
    )
    site = models.CharField(
        max_length=3,
        choices=SITE,
        blank=True,
        default='a',
        help_text='Site availability',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this video."""
        return reverse('video-detail', args=[str(self.id)])
