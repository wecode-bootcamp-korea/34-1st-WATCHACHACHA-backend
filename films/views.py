import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from films.models import Film

class FilmView(View):
    def get(self, request):
        try:
            genre            = request.GET.get('genre', None)
            country          = request.GET.get('country', None)
            running_time_min = request.GET.get('time', None)

            sort   = request.GET.get('sort')
            offset = int(request.GET.get('offset', 0))
            limit  = int(request.GET.get('limit', 10))

            q = Q()

            if genre:
                q &= Q(genres__name = genre)

            if country:
                q &= Q(countries__name = country)

            if running_time_min:
                q &= Q(running_time_min__lte = int(running_time_min))

            sort_set = {
                'random'          : '?',
                'ascending-time'  : 'running_time_min',
                'descending-time' : '-running_time_min',
                'score'           : 'rate_set__score'
            }

            order_key = sort_set.get(sort, 'id')

            films = Film.objects.filter(q).order_by(order_key)[offset:offset+limit]

            results = [{
                    'id'               : film.id,
                    'name'             : film.name,
                    'release_date'     : film.release_date.year,
                    'image_url'        : film.image_url,
                    'country'          : [country.name for country in film.countries.all()],
                    'running_time_min' : film.running_time_min,
                } for film in films]
            return JsonResponse({'results': results}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)

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
                        'name'      : actor.actor.name,
                        'image_url' : actor.actor.image_url,
                        'cast'      : actor.cast.name if actor.cast else None,
                        'role'      : actor.role.name
                    } for actor in film.filmactor_set.all()
                ]
            }
            return JsonResponse({'film': film}, status=200)
        except Film.DoesNotExist:
            return JsonResponse({'message': 'FILM_DOES_NOT_EXIST'}, status=400)

