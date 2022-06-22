from django.db import models

from films.models import Film
from core.models  import TimeStampModel

class User(TimeStampModel):
    email         = models.CharField(max_length=80, unique=True)
    password      = models.CharField(max_length=200)
    username      = models.CharField(max_length=80, unique=True)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'users'

class WatchList(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'watch_lists'

class Rate(models.Model):
    score = models.DecimalField(max_digits=2, decimal_places=1)
    film  = models.ForeignKey(Film, on_delete=models.CASCADE)
    user  = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'rates'
