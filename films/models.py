from django.db import models

class Film(models.Model):
    name             = models.CharField(max_length=100)
    release_date     = models.DateField()
    image_url        = models.URLField()
    running_time_min = models.IntegerField()
    description      = models.CharField(max_length=1000, default='')
    rating_system    = models.ForeignKey('RatingSystem', on_delete=models.CASCADE)

    class Meta:
        db_table = 'films'

class RatingSystem(models.Model):
    rate = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'rating_systems'

class Genre(models.Model):
    name  = models.CharField(max_length=50)
    film  = models.ManyToManyField(Film, through='FilmGenre', related_name='genres')

    class Meta:
        db_table = 'genres'

class Director(models.Model):
    name      = models.CharField(max_length=80)
    image_url = models.URLField(default='')
    film      = models.ManyToManyField(Film, through='FilmDirector', related_name='directors')

    class Meta:
        db_table = 'directors'

class Actor(models.Model):
    name      = models.CharField(max_length=80)
    image_url = models.URLField(default='')
    film      = models.ManyToManyField(Film, through='FilmActor', related_name='actors')

    class Meta:
        db_table = 'actors'

class Cast(models.Model):
    name = models.CharField(max_length=80, default='')

    class Meta:
        db_table = 'casts'

class Role(models.Model):
    name = models.CharField(max_length=80, default='')

    class Meta:
        db_table = 'roles'

class OttPlatform(models.Model):
    name  = models.CharField(max_length=50, default='')
    film  = models.ManyToManyField(Film, through='FilmOttPlatForm', related_name='ott_platforms')

    class Meta:
        db_table = 'ott_platforms'

class Country(models.Model):
    name  = models.CharField(max_length=50)
    film  = models.ManyToManyField(Film, through='FilmCountry', related_name='countries')

    class Meta:
        db_table = 'countries'

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
    cast  = models.ForeignKey('Cast', on_delete=models.CASCADE, default='')
    role  = models.ForeignKey('Role', on_delete=models.CASCADE, default='')

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
