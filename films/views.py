import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Avg

from films.models import Film
from users.models import Rate
from core.utils   import token_decorator

class FilmMainView(View):
    def get(self, request):
        try:
            film_data = [{
                'id'            : film.id,
                'name'          : film.name,
                'release_date'  : film.release_date,
                'image_url'     : film.image_url,
                'country'       : [country.name for country in film.countries.all()],
                'rating_system' : film.rating_system.rate,
                'score_average' : film.rate_set.aggregate(Avg('score'))['score__avg'],
            } for film in Film.objects.order_by('release_date')[:10]]
            return JsonResponse({'film_data': film_data}, status=201)
        except Film.DoesNotExist:
            return JsonResponse({'message': 'FILM_DOES_NOT_EXIST'}, status=400)
