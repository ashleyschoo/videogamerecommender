from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import django_filters
from django import forms
from django_filters.views import FilterView
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, redirect 
from django.template import loader
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.urls import re_path as url
from django.conf.urls import include
from django.views import generic
from django.views.generic.edit import FormView

from .models import VideoGames
from .models import AgeRating
from .models import GenreCategory
from .models import NumberofPlayers
from .models import PopularityRating
from .forms import forms
from games.forms import VideoGameForm
from games.forms import forms
from .filters import VideoGames
from .filters import VideoGamesFilter

# Create your views here.
def search(request):
    submitted = 'submitted' in request.GET
    data = request.GET if submitted else None
    VideoGames = VideoGamesFilter(data, queryset=VideoGames.objects.all())
    return render(request, 'games/game.html', {'VideoGames': VideoGames})  


def index(request):
    submitted = 'submitted' in request.GET
    latest_question_list = VideoGames.objects.order_by('VideoGameName')
    template = loader.get_template('games/home.html')
    output = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(output, request))   

def games_detail(request, VideoGameID):
    try:
        question = VideoGames.objects.get(pk=VideoGameID)
    except VideoGames.DoesNotExist:
        raise Http404("VideoGame does not exist")
    return render(request, 'games/game.html', {'VideoGames': VideoGames})     

class HomePageView(FilterView):
    template_name = 'games/home.html'
    filterset_class = VideoGamesFilter

# class QuestionPageView(generic.TemplateView):
#     template_name = 'games/questions.html'     


class VideoGamesFilterView(FilterView):
    #model = VideoGames
    filterset_class = VideoGamesFilter
    template_name = 'games/questions.html'
    #context_object_name = 'VideoGamesFiltered'    


class VideoGamesListView(generic.ListView):
    model = VideoGames
    context_object_name = 'VideoGames'
    template_name = 'games/game.html'
    
    def get_queryset(self):
        return VideoGames.objects.all().select_related('AgeRating', 'GenreCategory', 'NumberofPlayers', 'PopularityRating').order_by('VideoGameName').values()

