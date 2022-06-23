import re

from django.http            import JsonResponse
from django.core.exceptions import ValidationError

#USERNAME_REGEX: 한글/영어, 숫자x,기호x
USERNAME_REGEX = '^([A-Za-z0-9가-힣]{2,})+'
#EMAIL_REGEX: @와 .필수
EMAIL_REGEX    = '^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$'
#PASSWORD_REGEX: 10자 이상, 영,숫자,특수기호 중 2개 이상 포함
PASSWORD_REGEX = '^((?=.*[A-Za-z])(?=.*\d)|(?=.*[A-Za-z])(?=.*[\^@$!%*#?&])|(?=.*\d)(?=.*[\^@$!%*#?&])).{10,}$'
#BIRTH_REGEX: 1900~2099년생까지
BIRTH_REGEX    = '^(19[0-9][0-9]|20[0-9][0-9])*-(0[1-9]|1[0-2])*-(0[1-9]|[1-2][0-9]|3[0-1])$'

def validate_username(value):
    if not re.match(USERNAME_REGEX,value):
        raise ValidationError('INVALID_USERNAME')
def validate_email(value):
    if not re.match(EMAIL_REGEX,value):
        raise ValidationError('INVALID_EMAIL')
def validate_password(value):
    if not re.match(PASSWORD_REGEX,value):
        raise ValidationError('INVALID_PASSWORD')
def validate_birth(value):
    if not re.match(BIRTH_REGEX,value):
        raise ValidationError('INVALID_BIRTH')

