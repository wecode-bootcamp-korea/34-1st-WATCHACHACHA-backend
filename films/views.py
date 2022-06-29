import json

from django.http      import JsonResponse
from django.views     import View

from films.models import Film

class FilmDetailView(View):
    def get(self, request, film_id):
        try:
            film = Film.objects.get(id=film_id)
            film = {
                'id'               : film.id,
                'name'             : film.name,
                'release_date'     : film.release_date.year,
                'image_url'        : film.image_url,
                'running_time_min' : film.running_time_min,
                'descriptions'     : film.description,
                'genre'            : [genre.name for genre in film.genres.all()],
                'countries'        : [country.name for country in film.countries.all()],
                'directors' : [
                    {
                        'name'      : director.name,
                        'image_url' : director.image_url,
                        'role'      : '감독'
                    } for director in film.directors.all()
                ],
                'actors' : [
                    {
                        'name' : actor.actor.name,
                        'image_url' : actor.actor.image_url,
                        'cast' : actor.cast.name if actor.cast else None,
                        'role' : actor.role.name
                    } for actor in film.filmactor_set.all()
                ]
            }
            return JsonResponse({'film': film}, status=200)
        except Film.DoesNotExist:
            return JsonResponse({'message': 'FILM_DOES_NOT_EXIST'}, status=400)


