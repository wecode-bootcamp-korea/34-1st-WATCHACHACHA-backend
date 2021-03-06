import jwt

from django.http   import JsonResponse

from users.models            import User
from watcha_classic.settings import SECRET_KEY, ALGORITHM

def token_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload      = jwt.decode(access_token, SECRET_KEY, ALGORITHM)
            user         = User.objects.get(id=payload['id'])
            request.user = user
            return func(self, request, *args, **kwargs)

        except jwt.exceptions.InvalidSignatureError:
            return JsonResponse({'message' : 'INVALID_SIGNATURE_ERROR'}, status=401)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'DECODE_ERROR'}, status=401)

        except jwt.exceptions.InvalidTokenError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'USER_DOES_NOT_EXIST'}, status=401)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=401)
    return wrapper
