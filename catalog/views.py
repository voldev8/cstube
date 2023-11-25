from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponseRedirect

from catalog.models import Maps, Videos, Links

import requests
import environ
from pathlib import Path


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_maps = Maps.objects.all().count()
    num_videos = Videos.objects.filter(admin_permission=True).count()

    # with urllib.request.urlopen("https://www.reddit.com/r/GlobalOffensive/top.json?t=week") as url:
    #     data = json.loads(url.read().decode())

    # reddit_data = data['data']['children'][:10]
    context = {
        'num_maps': num_maps,
        'num_videos': num_videos,
        # 'reddit_data': reddit_data
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class MapView(generic.ListView):
    model = Maps


class MapDetailView(generic.DetailView):
    model = Maps


class LinkView(generic.ListView):
    model = Links

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the maps
        context['map_link_list'] = Maps.objects.all()
        return context


class LinkDetailView(generic.DetailView):
    model = Links

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the maps
        context['collections'] = Maps.objects.all()
        context['map_link_list_detail'] = get_object_or_404(
            Maps, pk=self.kwargs['pk'])
        return context


class VideoView(generic.ListView):
    model = Videos

    queryset = Videos.objects.filter(admin_permission=True)

    # def filter_map(self, map_name):
    #     return Videos.objects.filter(map_belong__icontains=map_name)


class VideoDetailView(generic.DetailView):
    model = Videos


def add_favorite_video(request, pk):
    if request.method == 'POST':
        favorite = Videos.objects.get(pk=pk)
        user = request.user
        user.favorite_videos.add(favorite)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_favorite_video(request, pk):
    if request.method == 'POST':
        favorite = Videos.objects.get(pk=pk)
        user = request.user
        user.favorite_videos.remove(favorite)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class SearchResultsView(generic.ListView):
    model = Videos
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        # object_list = Videos.objects.filter(
        #     Q(title__icontains=query) | Q(map_belong__name__icontains=query)
        # )
        object_list = Videos.objects.annotate(search=SearchVector(
            'title', 'map_belong__name')).filter(search=query, admin_permission=True)
        print(query)
        return object_list


class VideoCreate(CreateView):
    model = Videos
    fields = ['title', 'link', 'map_belong',
              'type_video', 'site']


def twitch(request):
    """
    top five twitch live streams - CS
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
            result['message'] = 'No entry found.'
        else:
            result['message'] = 'The Twitch API is not available at the moment.'
    context = {
        # 'links': ['https://www.twitch.tv/'+res['user_name'] for res in result['data']],
        'streams': result['data']
    }
    return render(request, 'twitch.html', context=context)


def twitch_auth():
    """
    function to get twitch token
    """
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    base = environ.Path(__file__) - 2  # two folders back (/a/b/ - 2 = /)
    env = environ.Env()
    # reading .env file  # reading .env file
    environ.Env.read_env(env_file=base('.env'))
    client_id = 'kg7560bqizr6ip9dk1y9lsd0xsw359'
    client_secret = env('TWITCH_CLIENT_SECRET')

    body = {
        'client_id': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)
    keys = r.json()

    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + keys['access_token']
    }
    return headers
