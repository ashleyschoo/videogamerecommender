# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class AgeRating(models.Model):
    AgeRatingid = models.AutoField(primary_key=True)
    AgeRating = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'AgeRating'
        ordering = ['AgeRating']
        verbose_name = 'AgeRating'
        verbose_name_plural = 'AgeRatings'

    def __str__(self):
        return self.AgeRating

class GenreCategory(models.Model):
    GenreCategoryid = models.AutoField(primary_key=True)
    GenreCategory = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'GenreCategory'
        ordering = ['GenreCategory']
        verbose_name = 'GenreCategory'
        verbose_name_plural = 'GenreCategories'

    def __str__(self):
        return self.GenreCategory


class NumberofPlayers(models.Model):
    NumberofPlayersid = models.AutoField(primary_key=True)
    NumberofPlayers = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'NumberofPlayers'
        ordering = ['NumberofPlayers']
        verbose_name = 'NumberofPlayers'
        verbose_name_plural = 'NumberofPlayers'

    def __str__(self):
        return self.NumberofPlayers

class PopularityRating(models.Model):
    PopularityRatingid = models.AutoField(primary_key=True)
    PopularityRating = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'PopularityRating'
        ordering = ['PopularityRating']
        verbose_name = 'PopularityRating'
        verbose_name_plural = 'PopularityRatings'

    def __str__(self):
        return self.PopularityRating


class VideoGames(models.Model):
    VideoGamesid = models.AutoField(primary_key=True)
    VideoGameName = models.CharField(unique=True, max_length=255)
    Description = models.CharField(max_length=255)
    YoutubeTrailerLink = models.CharField(max_length=255)
    PC_Windows = models.CharField(max_length=1)
    PC_MAC = models.CharField(max_length=1)
    Playstation = models.CharField(max_length=1)
    NintendoSwitch = models.CharField(max_length=1)
    Xbox = models.CharField(max_length=1)
    Phone_Android = models.CharField(max_length=1)
    Phone_iPhone = models.CharField(max_length=1)
    AgeRating = models.ForeignKey('AgeRating', models.DO_NOTHING, blank=True, null=True)
    GenreCategory = models.ForeignKey('GenreCategory', models.DO_NOTHING, blank=True, null=True)
    NumberofPlayers = models.ForeignKey('NumberofPlayers', models.DO_NOTHING, blank=True, null=True)
    PopularityRating = models.ForeignKey('PopularityRating', models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'VideoGames'
        ordering = ['VideoGamesid']
        verbose_name = 'VideoGame'
        verbose_name_plural = 'VideoGames'

    def __str__(self):
        return self.VideoGameName

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'pk': self.pk})
                    