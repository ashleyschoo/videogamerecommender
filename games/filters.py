import django_filters
from games.models import VideoGames, AgeRating, GenreCategory, NumberofPlayers, PopularityRating


class VideoGamesFilter(django_filters.FilterSet):
	#changes what form / filter boxes display on the page
	#MultipleChoiceFilter
	PC_Windows = django_filters.ChoiceFilter(
		#queryset=VideoGames.objects.all().order_by("PC_Windows"),
		field_name = 'PC_Windows',
		label = 'Will you be playing on a Windows PC?'
		)

	PC_MAC = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("PC_MAC"),
		field_name = 'PC_MAC',
		label = 'PC_MAC'
		)

	Playstation = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Playstation"),
		field_name='Playstation',
		label = 'Playstation'
		)

	NintendoSwitch = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("NintendoSwitch"),
		field_name='NintendoSwitch',
		label = 'NintendoSwitch'
		)

	Xbox = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Xbox"),
		field_name = 'Xbox',
		label = 'Xbox'
		)

	Phone_Android = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Phone_Android"),
		field_name='Phone_Android',
		label = 'Phone_Android'
		)


	Phone_iPhone = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Phone_iPhone"),
		field_name='Phone_iPhone',
		label = 'Phone_iPhone'
		)

	AgeRating = django_filters.ModelMultipleChoiceFilter(
		queryset=VideoGames.objects.all(),
		field_name='AgeRating__AgeRating',
		label='AgeRating'
		#widget=forms.CheckboxSelectMultiple()
		)
	GenreCategory = django_filters.ModelMultipleChoiceFilter(
		queryset=VideoGames.objects.all(),
		field_name='GenreCategory__GenreCategory',
		label='GenreCategory'
		#widget=forms.CheckboxSelectMultiple()
		)

	NumberofPlayers = django_filters.ModelMultipleChoiceFilter(
		queryset=VideoGames.objects.all(),
		field_name='NumberofPlayers__NumberofPlayers',
		label='NumberofPlayers'
		#widget=forms.CheckboxSelectMultiple()
		)

	PopularityRating = django_filters.ModelMultipleChoiceFilter(
		queryset=VideoGames.objects.all(),
		field_name='PopularityRating__PopularityRating',
		label='PopularityRating'
		#widget=forms.CheckboxSelectMultiple()
		)			
	class Meta:
		model = VideoGames
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []