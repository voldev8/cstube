from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.postgres.search import SearchVector

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

class SearchResultsView(generic.ListView):
    model = Videos
    template_name = 'search_results.html'
    def get_queryset(self): 
        query = self.request.GET.get('q')
        # object_list = Videos.objects.filter(
        #     Q(title__icontains=query) | Q(map_belong__name__icontains=query)
        # )
        object_list = Videos.objects.annotate(search=SearchVector('title', 'map_belong__name')).filter(search=query)
        print(query)
        return object_list

class VideoCreate(CreateView):
    model = Videos
    fields = ['title', 'link', 'map_belong', 'type_video', 'site']
