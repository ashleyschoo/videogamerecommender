import django_filters
from django import forms
from django.forms import forms
from django.utils.safestring import mark_safe
from games.models import VideoGames, AgeRating, GenreCategory, NumberofPlayers, PopularityRating

# Grab Distinct values for series
def getUniqueSeriesAgeRating():
     series_dicts = AgeRating.objects.all().values_list('AgeRating').distinct()
     series_list = []
     i = 1
     for item in series_dicts:
            series_list.append((i,item[0]))
            i = i+1
     return series_list

def getUniqueSeriesGenreCategory():
     series_dicts = GenreCategory.objects.all().values_list('GenreCategory').distinct()
     series_list = []
     i = 1
     for item in series_dicts:
            series_list.append((i,item[0]))
            i = i+1
     return series_list   

def getUniqueSeriesNumberofPlayers():
     series_dicts = NumberofPlayers.objects.all().values_list('NumberofPlayers').distinct()
     series_list = []
     i = 1
     for item in series_dicts:
            series_list.append((i,item[0]))
            i = i+1
     return series_list

def getUniqueSeriesPopularityRating():
     series_dicts = PopularityRating.objects.all().values_list('PopularityRating').distinct()
     series_list = []
     i = 1
     for item in series_dicts:
            series_list.append((i,item[0]))
            i = i+1
     return series_list 

class VideoGamesFilter(django_filters.FilterSet):
	#changes what form / filter boxes display on the page
	

	#MultipleChoiceFilter
	PC_Windows = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("PC_Windows"),
		#widget=django_filters.RadioSelect(choices=CHOICES),
		field_name = 'PC_Windows',
		label = mark_safe('Will you be playing on a Windows computer? <br/> Enter 1 for Yes, 0 for No<br/> Leave blank if you\'re indifferent')
		)

	PC_MAC = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("PC_MAC"),
		field_name = 'PC_MAC',
		label = mark_safe('Will you be playing on a MAC (Apple) computer? <br/> Enter 1 for Yes, 0 for No<br/> Leave blank if you\'re indifferent')
		)

	Playstation = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Playstation"),
		field_name='Playstation',
		label = mark_safe('Will you be playing on a Playstation? <br/> Enter 1 for Yes, 0 for No<br/> Leave blank if you\'re indifferent')
		)

	NintendoSwitch = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("NintendoSwitch"),
		field_name='NintendoSwitch',
		label = mark_safe('Will you be playing on a Nintendo Switch? <br/> Enter 1 for Yes, 0 for No<br/> Leave blank if you\'re indifferent')
		)

	Xbox = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Xbox"),
		field_name = 'Xbox',
		label = mark_safe('Will you be playing on an Xbox?<br />Enter 1 for Yes, 0 for No<br/> Leave blank if you\'re indifferent')
		)

	Phone_Android = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Phone_Android"),
		field_name='Phone_Android',
		label = mark_safe('Will you be playing on an Android phone?<br />Enter 1 for Yes, 0 for No<br/> Leave blank if you\'re indifferent')
		)


	Phone_iPhone = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Phone_iPhone"),
		field_name='Phone_iPhone',
		label = mark_safe('Will you be playing on an iPhone?<br />Enter 1 for Yes, 0 for No<br/> Leave blank if you\'re indifferent')
		)

	AgeRating = django_filters.MultipleChoiceFilter(
		choices = getUniqueSeriesAgeRating(),
		#queryset=VideoGames.objects.all().values_list('AgeRating').distinct(),
		#field_name='AgeRating__AgeRating',
		label = mark_safe('What age category do the players belong to? <br /> Hold "shift" to select multiple: ')
		#widget=forms.CheckboxSelectMultiple()
		)
	GenreCategory = django_filters.MultipleChoiceFilter(
		choices = getUniqueSeriesGenreCategory(),
		#queryset=GenreCategory.objects.all().values_list('GenreCategory').distinct(),
		#field_name='GenreCategory__GenreCategory',
		label = mark_safe('Select a game genre.  <br /> Hold "shift" to select multiple:  ')
		#widget=forms.CheckboxSelectMultiple()
		)

	NumberofPlayers = django_filters.MultipleChoiceFilter(
		choices = getUniqueSeriesNumberofPlayers(),
		#queryset=NumberofPlayers.objects.all().values_list('NumberofPlayers').distinct(),
		#field_name='NumberofPlayers__NumberofPlayers',
		label = mark_safe('Will the game be played alone or with friends? <br /> Select the number of players: ')
		#widget=forms.CheckboxSelectMultiple()
		)

	# PopularityRating = django_filters.MultipleChoiceFilter(
	# 	choices = getUniqueSeriesPopularityRating(),
	# 	#queryset=VideoGames.objects.values_list('PopularityRating').distinct(),
	# 	#field_name='PopularityRating__PopularityRating',
	# 	label='Choose a popularity rating: '
	# 	#widget=forms.CheckboxSelectMultiple()
	# 	)			
	class Meta:
		model = VideoGames
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = ['NumberofPlayers', 'AgeRating','GenreCategory',
		'PC_Windows','PC_MAC', 'Playstation','NintendoSwitch','Xbox','Phone_Android','Phone_iPhone'
		]
		#,'PopularityRating']