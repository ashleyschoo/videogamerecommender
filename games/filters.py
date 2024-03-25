import django_filters
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
		field_name = 'PC_Windows',
		label = 'Will you be playing on a Windows computer? \n Enter 1 for Yes, 0 for No'
		)

	PC_MAC = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("PC_MAC"),
		field_name = 'PC_MAC',
		label = 'Will you be playing on a MAC (Apple) computer? \n Enter 1 for Yes, 0 for No'
		)

	Playstation = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Playstation"),
		field_name='Playstation',
		label = 'Will you be playing on a Playstation? \n Enter 1 for Yes, 0 for No'
		)

	NintendoSwitch = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("NintendoSwitch"),
		field_name='NintendoSwitch',
		label = 'Will you be playing on a Nintendo Switch? \n Enter 1 for Yes, 0 for No'
		)

	Xbox = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Xbox"),
		field_name = 'Xbox',
		label = 'Will you be playing on an Xbox? \n Enter 1 for Yes, 0 for No'
		)

	Phone_Android = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Phone_Android"),
		field_name='Phone_Android',
		label = 'Will you be playing on an Android phone? \\n Enter 1 for Yes, 0 for No'
		)


	Phone_iPhone = django_filters.CharFilter(
		#queryset=VideoGames.objects.all().order_by("Phone_iPhone"),
		field_name='Phone_iPhone',
		label = 'Will you be playing on an iPhone? \n Enter 1 for Yes, 0 for No'
		)

	AgeRating = django_filters.MultipleChoiceFilter(
		choices = getUniqueSeriesAgeRating(),
		#queryset=VideoGames.objects.all().values_list('AgeRating').distinct(),
		#field_name='AgeRating__AgeRating',
		label='What age category do the players belong to?'
		#widget=forms.CheckboxSelectMultiple()
		)
	GenreCategory = django_filters.MultipleChoiceFilter(
		choices = getUniqueSeriesGenreCategory(),
		#queryset=GenreCategory.objects.all().values_list('GenreCategory').distinct(),
		#field_name='GenreCategory__GenreCategory',
		label='Select a game genre: '
		#widget=forms.CheckboxSelectMultiple()
		)

	NumberofPlayers = django_filters.MultipleChoiceFilter(
		choices = getUniqueSeriesNumberofPlayers(),
		#queryset=NumberofPlayers.objects.all().values_list('NumberofPlayers').distinct(),
		#field_name='NumberofPlayers__NumberofPlayers',
		label='Select the number of players: '
		#widget=forms.CheckboxSelectMultiple()
		)

	PopularityRating = django_filters.MultipleChoiceFilter(
		choices = getUniqueSeriesPopularityRating(),
		#queryset=VideoGames.objects.values_list('PopularityRating').distinct(),
		#field_name='PopularityRating__PopularityRating',
		label='Choose a popularity rating: '
		#widget=forms.CheckboxSelectMultiple()
		)			
	class Meta:
		model = VideoGames
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = ['PC_Windows','PC_MAC', 'Playstation','NintendoSwitch','Xbox','Phone_Android','Phone_iPhone', 'AgeRating',
		'GenreCategory','NumberofPlayers','PopularityRating']