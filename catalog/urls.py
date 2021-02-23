from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maps/', views.MapView.as_view(), name='maps'),
    path('map/<int:pk>', views.MapDetailView.as_view(), name='map-detail'),
    path('videos/', views.VideoView.as_view(), name='videos'),
]
