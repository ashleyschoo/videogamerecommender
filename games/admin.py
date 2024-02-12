from django.contrib import admin

# Register your models here.
import games.models as models


# admin.site.VideoGames
@admin.register(models.VideoGames)
class VideoGames(admin.ModelAdmin):
	fieldsets = (
			(None, {
				'fields': (
				'VideoGameName',
				'PC(Windows)',
				'PC(MAC)',
				'Playstation',	
				'NintendoSwitch',
				'Xbox',
				'Phone(Android)',
				'Phone(iPhone)',
				'Description',
				'YouTubeTrailerLink'
				)
				}),
			# ('AgeRating', {
			# 	'fields': [
			# 		(
			# 		'AgeRating'
			# 		)],
			# 		})
			# ('GenreCategory', {
			# 	'fields': [
			# 		(
			# 		'GenreCategory'
			# 		)],
			# 		})
			# ('NumberofPlayers', {
			# 	'fields': [
			# 		(
			# 		'NumberofPlayers'
			# 		)],
			# 		})
			# ('PopularityRating', {
			# 	'fields': [
			# 		(
			# 		'PopularityRating'
			# 		)]
			# 		})													
)

# may need to add the foreign key here from the joining table
	list_display = (
		'AgeRating',
		'GenreCategory',
		'PopularityRating',
		'NumberofPlayers'
		)

	list_filter = (
		'AgeRating',
		'GenreCategory',
		'PopularityRating',
		'NumberofPlayers'
		)



#  admin.site.AgeRating
@admin.register(models.AgeRating)
class AgeRating(admin.ModelAdmin):
	fields = ['AgeRating']
	list_display = ['AgeRating']
	ordering = ['AgeRating']

#  admin.site.GenreCategory
@admin.register(models.GenreCategory)
class GenreCategory(admin.ModelAdmin):
	fields = ['GenreCategory']
	list_display = ['GenreCategory']
	ordering = ['GenreCategory']

#  admin.site.NumberofPlayers
@admin.register(models.NumberofPlayers)
class NumberofPlayers(admin.ModelAdmin):
	fields = ['NumberofPlayers']
	list_display = ['NumberofPlayers']
	ordering = ['NumberofPlayers']

#  admin.site.PopularityRating
@admin.register(models.PopularityRating)
class PopularityRating(admin.ModelAdmin):
	fields = ['PopularityRating']
	list_display = ['PopularityRating']
	ordering = ['PopularityRating']


