from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('twitch/', views.twitch, name='twitch'),
    path('links/', views.LinkView.as_view(), name='links'),
    path('map_link/<int:pk>', views.LinkDetailView.as_view(), name='link-detail'),
    path('maps/', views.MapView.as_view(), name='maps'),
    path('map/<int:pk>', views.MapDetailView.as_view(), name='map-detail'),
    path('videos/', views.VideoView.as_view(), name='videos'),
    path('videos/<int:pk>', views.VideoDetailView.as_view(), name='videos-detail'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('videos/create/', views.VideoCreate.as_view(), name='video-create'),
]
