from django.http      import JsonResponse
from django.views     import View

from films.models     import Film

class FilmView(View):
    def get(self, request):
        # --- 국가 별 query string ---
        # localhost:8000/films?country=한국                                  # 1. 한국 / 2. 미국
        # localhost:8000/films?country=미국
        try:
            country          = request.GET.get('country')
            country_of_films = Film.objects.filter(countries__name=country)
            results = [{
                'id'               : film.id,
                'name'             : film.name,
                'release_date'     : film.release_date.year,
                'image_url'        : film.image_url,
                'country'          : [country.name for country in film.countries.all()],
                'running_time_min' : film.running_time_min,
            } for film in country_of_films[:10]]
            return JsonResponse({'results': results}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'})

        # --- 장르 별 query string ---
        # localhost:8000/films?genre=드라마
        # localhost:8000/films?genre=로맨스

            # genre          = request.GET.get('genre')                           # 1. 드라마 / 2. 로맨스
            # genre_of_films = Film.objects.filter(genres__name=genre)
            # results = [{
            #     'id'               : film.id,
            #     'name'             : film.name,
            #     'release_date'     : film.release_date.year,
            #     'image_url'        : film.image_url,
            #     'country'          : [country.name for country in film.countries.all()],
            #     'running_time_min' : film.running_time_min,
            # } for film in genre_of_films[:10]]
            # return JsonResponse({'results': results}, status=201)
