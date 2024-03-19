from django.urls import path, re_path as url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.HomePageView.as_view(), name='home'),
    path('questions/', views.VideoGamesFilterView.as_view(), name='questions'),
    #path('resultsfilter/', views.VideoGamesFilterView.as_view(), kwargs=None, name='resultsfilter'),
    #path('games_detail/', views.FilterView.as_view(), kwargs=None, name='games_detail'),
    path('game/', views.VideoGamesListView.as_view(), kwargs=None, name='game'),


]