from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.postgres.search import SearchVector

from catalog.models import Maps, Videos
import requests
import environ
from pathlib import Path

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

def twitch(request):
    """
    top five twitch live streams - CS:GO
    """
    headers = twitch_auth()

    result = {}
    url = 'https://api.twitch.tv/helix/streams?game_id=32399&first=5'

    response = requests.get(url, headers=headers)
    if response.status_code == 200:  # SUCCESS
        result = response.json()
        result['success'] = True
    else:
        result['success'] = False
        if response.status_code == 404:  # NOT FOUND
            result['message'] = 'No entry found for "%s"' % word
        else:
            result['message'] = 'The Twitch API is not available at the moment.'
    context = {
        # 'links': ['https://www.twitch.tv/'+res['user_name'] for res in result['data']],
        'streams': result['data']
    }
    return render(request, 'twitch.html', context=context)

class MapView(generic.ListView):
    model = Maps

class MapDetailView(generic.DetailView):
    model = Maps

class VideoView(generic.ListView):
    model = Videos

    def filter_map(self, map_name):
        return Videos.objects.filter(map_belong__icontains=map_name)

class VideoDetailView(generic.DetailView):
    model = Videos
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


def twitch_auth():
    """
    function to get twitch token
    """
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    base = environ.Path(__file__) - 2 # two folders back (/a/b/ - 2 = /)
    env = environ.Env()
    environ.Env.read_env(env_file=base('.env')) # reading .env file  # reading .env file
    client_id = 'kg7560bqizr6ip9dk1y9lsd0xsw359'
    client_secret = env('TWITCH_CLIENT_SECRET')

    body = {
        'client_id': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)
    keys = r.json();

    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + keys['access_token']
    }
    return headers