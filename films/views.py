import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Avg

from films.models import (
    Film, RatingSystem, Genre, Director, Actor, Cast, Role, OttPlatform, Country,
    FilmGenre, FilmDirector, FilmActor, FilmCountry
    )

class FilmDetailView(View):
    def get(self, request, film_id):
        try:
            films = Film.objects.get(id=film_id)
            # rating_systems는 구현 보류
            # rating_systems = RatingSystem.objects.get(id=films.rating_system_id)
            #genres는 한 리스트에 두기 위해 따로 변수로 지정
            genres = [firms_genres.genre.name for firms_genres in FilmGenre.objects.filter(film_id=film_id)]

            film = {
                'id'               : films.id,
                'name'             : films.name,
                'release_date'     : films.release_date.year,
                'image_url'        : films.image_url,
                'running_time_min' : films.running_time_min,
                'descriptions'     : films.description,
                'genres'           : genres,
                'countries'        : [films_countries.country.name for films_countries in FilmCountry.objects.filter(film_id=film_id)],
                'directors' : [
                    {
                        'name' : films_directors.director.name,
                        'image_url' : films_directors.director.image_url,
                        'role' : '감독'
                    } for films_directors in FilmDirector.objects.filter(film_id=film_id)
                ],
                'actors' : [
                    {
                        'name' : films_actors.actor.name,
                        'image_url' : films_actors.actor.image_url,
                        'cast' : films_actors.cast.name if films_actors.cast else None,
                        'role' : films_actors.role.name
                    } for films_actors in FilmActor.objects.filter(film_id=film_id)
                ]
            # rate는 구현 보류
            # rate = {
            #     'rating_systems' : rating_systems.rate
            # }
            }
            return JsonResponse({'film': film}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEYERROR'}, status=400)
        except Film.DoesNotExist:
            return JsonResponse({'message': 'FILM_DOES_NOT_EXIST'}, status=400)