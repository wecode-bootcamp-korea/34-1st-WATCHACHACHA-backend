from django.http      import JsonResponse
from django.views     import View

from films.models     import Film

class FilmView(View):
    def get(self, request):
        try:
            genre            = request.GET.get('genre')
            country          = request.GET.get('country')
            running_time_min = int(request.GET.get('time'))

            genre_of_films    = Film.objects.filter(genres__name = genre)
            country_of_films  = Film.objects.filter(countries__name = country)
            min_below_hundred = Film.objects.filter(running_time_min__lte = running_time_min)

            results = {
                'drama' : [{
                    'id'               : film.id,
                    'name'             : film.name,
                    'release_date'     : film.release_date.year,
                    'image_url'        : film.image_url,
                    'country'          : [country.name for country in film.countries.all()],
                    'running_time_min' : film.running_time_min,
                } for film in genre_of_films[:10]],
                'america' : [{
                    'id'               : film.id,
                    'name'             : film.name,
                    'release_date'     : film.release_date.year,
                    'image_url'        : film.image_url,
                    'country'          : [country.name for country in film.countries.all()],
                    'running_time_min' : film.running_time_min,
                } for film in country_of_films[:10]],
                'running_time_below_hundred' : [{
                    'id'               : film.id,
                    'name'             : film.name,
                    'release_date'     : film.release_date.year,
                    'image_url'        : film.image_url,
                    'country'          : [country.name for country in film.countries.all()],
                    'running_time_min' : film.running_time_min,
                } for film in min_below_hundred[:10]]
            }
            return JsonResponse({'results': results}, status = 201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status = 400)
