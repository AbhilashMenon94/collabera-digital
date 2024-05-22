from django.db import models
from django.utils.translation import gettext_lazy as _


class MovieGenre(models.Model):
    genre = models.CharField(verbose_name='Genre', max_length=100)

class DirectorModel(models.Model):
    name = models.CharField(verbose_name='Director', max_length=200)

class WriterModel(models.Model):
    name = models.CharField(verbose_name='Writer', max_length=200)

class ActorModel(models.Model):
    name = models.CharField(verbose_name='Actor', max_length=200)

class LanguageModel(models.Model):
    name = models.CharField(verbose_name='Language', max_length=200)

class CountryModel(models.Model):
    name = models.CharField(verbose_name='Country', max_length=200)

class MovieModel(models.Model):
    class AgeRating(models.TextChoices):
        NOT_AVAILABLE = "N/A", _("NOT_AVAILABLE")
        UNRATED = "Unrated", _("UNRATED")
        R_RATED = "R", _("R_RATED")
        PG_13 = "PG-13", _("PG_13")
        NOT_RATED = "Not Rated", _("NOT_RATED")
        TV_14 = "TV-14", _("TV_14")
        PG = "PG", _("PG")

    title = models.CharField(verbose_name='Title', max_length=200)
    year = models.IntegerField(verbose_name='Year')
    rated = models.CharField(
        max_length=12,
        choices=AgeRating,
        default=AgeRating.NOT_AVAILABLE,
    )
    released = models.DateField(verbose_name='Release Date')
    runtime = models.IntegerField(verbose_name='Runtime')
    director = models.ManyToManyField(DirectorModel)
    writer =  models.ManyToManyField(WriterModel)
    actors =  models.ManyToManyField(ActorModel)
    plot = models.TextField(verbose_name='Plot')
    language = models.ManyToManyField(LanguageModel)
    country = models.ManyToManyField(CountryModel)
    awards = models.TextField(verbose_name='Awards')
    poster = models.URLField (verbose_name='Poster')
    meta_score = models.CharField(verbose_name='Meta Score', max_length=16)
    imdb_rating = models.DecimalField(verbose_name='IMDB Rating', max_digits=2, decimal_places=1)
    imdb_votes = models.BigIntegerField(verbose_name='IMDB Votes')
    imdb_id = models.CharField(verbose_name='IMDB Id', max_length=16)
    type = models.CharField(verbose_name='Type', max_length=16)
    dvd = models.DateField(verbose_name='DVD Release Date', null=True)
    box_office = models.BigIntegerField(verbose_name='Box Office')
    production = models.CharField(verbose_name='Production', max_length=128)
    website = models.URLField(verbose_name='Website')
    genre = models.ManyToManyField(MovieGenre)
    ratings = models.JSONField()
    date = models.DateTimeField(verbose_name='Date', null=True)
