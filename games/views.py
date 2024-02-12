from games.forms import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question
from django.http import Http404
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.forms import ModelForm
from games.forms import forms
import django_filters
from django_filters.views import FilterView
from django.conf.urls import include
from django.urls import re_path as url
from django_filters.views import FilterView

from .models import VideoGames
from .models import AgeRating
from .models import GenreCategory
from .models import NumberofPlayers
from .models import PopularityRating
from .forms import VideoGameForm
from .filters import VideoGames

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the games index.")

def index(request):
    latest_question_list = VideoGames.objects.order_by('-pub_date')[:5]
    template = loader.get_template('games/questions.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))   

def detail(request, VideoGameid):
    try:
        question = VideoGames.objects.get(pk=VideoGamesid)
    except VideoGames.DoesNotExist:
        raise Http404("VideoGame does not exist")
    return render(request, 'games/detail.html', {'VideoGames': VideoGames})     

class HomePageView(generic.TemplateView):
    template_name = 'games/home.html'

class AboutPageView(generic.TemplateView):
    template_name = 'games/about.html'  

class QuestionPageView(generic.TemplateView):
    template_name = 'games/results_filter.html'     

class FilterView(FilterView):
    model = VideoGames
    filterset_class = FilterView
    template_name = 'games/results_filter.html'
    context_object_name = 'VideoGames'      