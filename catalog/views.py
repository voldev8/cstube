from django.shortcuts import render, get_object_or_404
from django.views import generic

from catalog.models import Maps, Videos


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_maps = Maps.objects.all().count()
    num_videos = Videos.objects.all().count()

    context = {
        'num_maps': num_maps,
        'num_videos': num_videos,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class MapView(generic.ListView):
    model = Maps

class MapDetailView(generic.DetailView):
    model = Maps

class VideoView(generic.ListView):
    model = Videos

    def filter_map(self, map_name):
        return Videos.objects.filter(map_belong__icontains=map_name)
