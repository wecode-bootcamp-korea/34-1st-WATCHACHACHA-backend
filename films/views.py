import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Avg

from films.models import Film

class FilmDetailView(View):
    def get(self, request, film_id):
        """
        request.GET = {
            "genre" : 'aa',
            "country" : 20

        }

        a = request.GET["genree"]
        """
        
        try:
            film = Film.objects.annotate(ave_score=Avg('rate__score')).get(id=film_id)

            film = {
                'id'               : film.id,
                'name'             : film.name,
                'release_date'     : film.release_date.year,
                'image_url'        : film.image_url,
                'running_time_min' : film.running_time_min,
                'descriptions'     : film.description,
                'average_score'    : film.avg_score,
                'genres'           : [genres.genre.name for genres in film.genres.all()],
                'countries'        : [country.country.name for country in film.countries.all()],
                'directors' : [
                    {
                        'name'      : director.director.name,
                        'image_url' : director.director.image_url,
                        'role'      : '감독'
                    } for director in film.directors.all()
                ],
                'actors' : [
                    {
                        'name'      : actor.actor.name,
                        'image_url' : actor.actor.image_url,
                        'cast'      : actor.cast.name if actor.cast else None,
                        'role'      : actor.role.name
                    } for actor in film.actors.all()
                ]
            }
            return JsonResponse({'film': film}, status=200)

        except Film.DoesNotExist:
            return JsonResponse({'message': 'FILM_DOES_NOT_EXIST'}, status=400)