import json

import bcrypt
import jwt
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError
from django.conf            import settings

from users.models     import User, WatchList
from films.models     import Film
from users.validation import (
    validate_username,
    validate_email,
    validate_password,
    validate_birth
)
from core.utils       import token_decorator

class SignUpView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)

            email         = data['email']
            password      = data['password']
            username      = data['username']
            date_of_birth = data['date_of_birth']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'EMAIL_ALREADY_EXISTS'}, status=409)

            validate_username(username)
            validate_email(email)
            validate_password(password)
            validate_birth(date_of_birth)

            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            User.objects.create(
                username      = username,
                email         = email,
                password      = hashed_password.decode('utf-8'),
                date_of_birth = date_of_birth,
            )
            return JsonResponse({'message' :'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' :'KEY_ERROR'}, status = 400)

        except ValidationError as error:
            return JsonResponse({'message' : error.message}, status = 400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

            access_token = jwt.encode({"id" : user.id}, settings.SECRET_KEY, algorithm = settings.ALGORITHM)

            return JsonResponse({'access_token' : access_token}, status = 200)

        except KeyError:
            return JsonResponse({'message' :'KEY_ERROR'}, status = 400)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

class WatchListView(View):
    @token_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not Film.objects.filter(id = data['film_id']).exists:
                return JsonResponse({'message' : 'FILM_DOES_NOT_EXIST'}, status = 404)

            film = Film.objects.get(id = data['film_id'])
            user = request.user

            wish, is_created = WatchList.objects.get_or_create(film = film, user = user)

            if not is_created:
                wish.delete()
                return JsonResponse({'message' : 'WATCH_LIST_DELETED'}, status = 204)

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' :'KEY_ERROR'}, status = 400)

    @token_decorator
    def get(self, request):
        user = request.user
        sort = request.GET.get('sort')

        sort_set = {
            'film'            : 'id',
            'random'          : '?',
            'score'           : 'rate_set__score',
            'time-ascending'  : 'running_time_min',
            'time-descending' : '-running_time_min',
        }

        order_key = sort_set.get(sort, '-watchlist__id')

        films = Film.objects.filter(watchlist__user=user).order_by(order_key)

        results = [{
            'id'               : film.id,
            'name'             : film.name,
            'image_url'        : film.image_url
        } for film in films]
        return JsonResponse({'results': results}, status=200)

class UserView(View):
    @token_decorator
    def get(self, request):
        try:
            user = request.user

            results = {
                'username'        : user.username,
                'watchlist_count' : user.watchlist_set.count(),
            }
            return JsonResponse({'results' : results})

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
