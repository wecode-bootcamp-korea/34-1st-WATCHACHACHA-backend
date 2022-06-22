from platform import release
from django.db import models

# 영화 테이블

class Film(models.Model):
    name             = models.CharField(max_length=100)
    release_date     = models.DateField()
    image_url        = models.URLField()
    running_time_min = models.CharField(max_length=20, default='')
    descriptions     = models.CharField(max_length=1000, default='')
    rating_systems   = models.ForeignKey('RatingSystem', on_delete=models.CASCADE)

    class Meta:
        db_table = 'films'

# 일대다 관계 테이블

class RatingSystem(models.Model):
    rate = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'rating_systems'

# 다대다 관계 테이블

class Genre(models.Model):
    name  = models.CharField(max_length=50)
    films = models.ManyToManyField(Film, through='FilmGenre')

    class Meta:
        db_table = 'genres'

class Director(models.Model):
    name      = models.CharField(max_length=80)
    image_url = models.URLField(default='')
    films     = models.ManyToManyField(Film, through='FilmDirector')

    class Meta:
        db_table = 'directors'

class Actor(models.Model):
    name      = models.CharField(max_length=80)
    image_url = models.URLField(default='')
    films     = models.ManyToManyField(Film, through='FilmActor')

    class Meta:
        db_table = 'actors'

class OttPlatform(models.Model):
    name  = models.CharField(max_length=50, default='')
    films = models.ManyToManyField(Film, through='FilmOttPlatForm')

    class Meta:
        db_table = 'ott_platforms'

class Country(models.Model):
    name  = models.CharField(max_length=50)
    films = models.ManyToManyField(Film, through='FilmCountry')

    class Meta:
        db_table = 'countries'

# 중간 테이블

class FilmGenre(models.Model):
    film  = models.ForeignKey('Film', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        db_table = 'films_genres'

class FilmDirector(models.Model):
    film     = models.ForeignKey('Film', on_delete=models.CASCADE)
    director = models.ForeignKey('Director', on_delete=models.CASCADE)

    class Meta:
        db_table = 'films_directors'

class FilmActor(models.Model):
    film  = models.ForeignKey('Film', on_delete=models.CASCADE)
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE)

    class Meta:
        db_table = 'films_actors'

class FilmOttPlatform(models.Model):
    film         = models.ForeignKey('Film', on_delete=models.CASCADE)
    ott_platform = models.ForeignKey('OttPlatform', on_delete=models.CASCADE)

    class Meta:
        db_table = 'films_ott_platforms'

class FilmCountry(models.Model):
    film    = models.ForeignKey('Film', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    class Meta:
        db_table = 'films_countries'
