import json
import re

import bcrypt
import jwt
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError
from django.conf            import settings

from users.models       import User, WatchList
from users.validation   import (
    validate_username,
    validate_email,
    validate_password,
    validate_birth
)

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
            return JsonResponse({'message':'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except ValidationError as error:
            return JsonResponse({'message': error.message}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)

            access_token = jwt.encode({"id" : user.id}, settings.SECRET_KEY, algorithm = settings.ALGORITHM)

            return JsonResponse({'access_token' : access_token}, status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

