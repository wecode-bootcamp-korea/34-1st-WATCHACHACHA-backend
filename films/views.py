from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from films.models import Film

#:8000/films?genre=공포
#:8000/films?country=미국
#:8000/films?country=미국&genre=블록버스터


class FilmView(View):
    def get(self, request):
        try:
            genre            = request.GET.get('genre')
            country          = request.GET.get('country')
            sort             = request.GET.get('sort')
            running_time_min = int(request.GET.get('time'))
            offset           = int(request.GET.get('offset', 0))
            limit            = int(request.GET.get('limit', 10))

            q = Q()

            if genre:
                q &= Q(genre__name = genre)

            if country:
                q &= Q(country__name = country)

            if running_time_min:
                q &= Q(running_time_min__lte = running_time_min)

            sort_set = {
                'running_time' : 'running_time_min',
                'star'         : 'point'
            }

            order_key = sort_set.get(sort, 'id')

            films = Film.objects.filter(q).order_by(order_key)[offset:offset+limit]

            results = {
                'films' : [{
                    'id'               : film.id,
                    'name'             : film.name,
                    'release_date'     : film.release_date.year,
                    'image_url'        : film.image_url,
                    'country'          : [country.name for country in film.countries.all()],
                    'running_time_min' : film.running_time_min,
                } for film in films]
            }
            return JsonResponse({'results': results}, status = 200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)
