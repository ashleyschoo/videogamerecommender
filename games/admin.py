from django.contrib import admin

# Register your models here.
import games.models as models


# admin.site.VideoGames
@admin.register(models.VideoGames)
class VideoGames(admin.ModelAdmin):
	fields = [	'VideoGameID',
				'VideoGameName',
				'PC_Windows',
				'PC_MAC',
				'Playstation',	
				'NintendoSwitch',
				'Xbox',
				'Phone_Android',
				'Phone_iPhone',
				'Description',
				'YouTubeTrailerLink',
				'AgeRating',
				'GenreCategory',
				'PopularityRating',
				'NumberofPlayers'
				]												

	# may need to add the foreign key here from the joining table
	list_display = [
				'VideoGameID',
				'VideoGameName',
				'PC_Windows',
				'PC_MAC',
				'Playstation',	
				'NintendoSwitch',
				'Xbox',
				'Phone_Android',
				'Phone_iPhone',
				'Description',
				'YouTubeTrailerLink',
				'AgeRating',
				'GenreCategory',
				'PopularityRating',
				'NumberofPlayers'
				]

	list_filter = [
				'AgeRating',
				'GenreCategory',
				'PopularityRating',
				'NumberofPlayers'
				]



#  admin.site.AgeRating
@admin.register(models.AgeRating)
class AgeRating(admin.ModelAdmin):
	fields = ['AgeRating']
	list_display = ['AgeRating']
	ordering = ['AgeRating_ID']

#  admin.site.GenreCategory
@admin.register(models.GenreCategory)
class GenreCategory(admin.ModelAdmin):
	fields = ['GenreCategory']
	list_display = ['GenreCategory']
	ordering = ['GenreCategory_ID']

#  admin.site.NumberofPlayers
@admin.register(models.NumberofPlayers)
class NumberofPlayers(admin.ModelAdmin):
	fields = ['NumberofPlayers']
	list_display = ['NumberofPlayers']
	ordering = ['NumberofPlayers_ID']

#  admin.site.PopularityRating
@admin.register(models.PopularityRating)
class PopularityRating(admin.ModelAdmin):
	fields = ['PopularityRating']
	list_display = ['PopularityRating']
	ordering = ['PopularityRating_ID']


