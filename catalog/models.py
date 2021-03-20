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
    class Meta:
        verbose_name="Map"


class Videos(models.Model):
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(
        max_length=300, 
        # help_text='Enter the link'
        )
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
        # help_text='Pick a type',
    )
    site = models.CharField(
        max_length=3,
        choices=SITE,
        blank=True,
        default='a',
        # help_text='Site availability',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this video."""
        return reverse('videos')
    def youtube_id(self):
        link = self.link.split('/')[-1]
        link_arr = link.split('?')
        youtube_id = link_arr[0] + '?star' + link_arr[1]
        return youtube_id
    class Meta:
        verbose_name = 'Video'
