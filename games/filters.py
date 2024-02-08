import django_filters
from games.models import VideoGames, AgeRating, GenreCategory, NumberofPlayers, PopularityRating

class FilterView(django_filters.FilterSet):
	VideoGameID = django_filters.CharFilter(
		field_name='VideoGames__VideoGameID',
		label='VideoGameID',
		lookup_expr='exact'
		)

	AgeRating = django_filters.ModelChoiceFilter(
		queryset=AgeRating.objects.all(),
		field_name='AgeRatingID',
		label='AgeRating',
		)
	GenreCategory = django_filters.ModelChoiceFilter(
		queryset=GenreCategory.objects.all(),
		field_name='GenreCategoryID',
		label='GenreCategory',
		)
	NumberofPlayers = django_filters.ModelChoiceFilter(
		queryset=NumberofPlayers.objects.all(),
		field_name='NumberofPlayersID',
		label='NumberofPlayers',
		)
	PopularityRating = django_filters.ModelChoiceFilter(
		queryset=PopularityRating.objects.all(),
		field_name='PopularityRatingID',
		label='PopularityRating',
		)

	class Meta:
		model = games
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = ['VideoGameID','AgeRating','GenreCategory','NumberofPlayers','PopularityRating']


class VideoGameNameFilterView(django_filters.FilterSet):
	VideoGameName = django_filters.CharFilter(
		field_name='VideoGameName',
		label='VideoGameName',
		lookup_expr='icontains'
	)

	# Add filters here
	Description = django_filters.CharFilter(
		field_name='Description',
		label='Description',
		lookup_expr='icontains'

		)
	YouTubeTrailerLink = django_filters.CharFilter(
		field_name = 'YouTubeTrailerLink',
		label='YouTubeTrailerLink',
		lookup_expr='icontains'
		)



	PC(Windows) = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("PC(Windows)"),
		field_name = 'PC(Windows)',
		label = 'PC(Windows)',
		)
	PC(MAC) = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("PC(MAC)"),
		field_name = 'PC(MAC)',
		label = 'PC(MAC)',
		)

	Playstation = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Playstation"),
		field_name='Playstation',
		label = 'Playstation',
		)


	NintendoSwitch = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("NintendoSwitch"),
		field_name='NintendoSwitch',
		label = 'NintendoSwitch',
		)

	Xbox = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Xbox"),
		field_name = 'Xbox',
		label = 'Xbox',
		)

	Phone(Android) = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Phone(Android)"),
		field_name='Phone(Android)',
		label = 'Phone(Android)',
		)


	Phone(iPhone) = django_filters.ModelChoiceFilter(
		queryset=VideoGames.objects.all().order_by("Phone(iPhone)"),
		field_name='Phone(iPhone)',
		label = 'Phone(iPhone)',
		)

	class Meta:
		model = games
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []