from django.db import models
from django.forms import CharField

from films.models import Film
from users.models import User

class TimeStampModel(models.Model):
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Comment(TimeStampModel):
    contents   = models.CharField(max_length=500)
    deleted_at = models.DateTimeField()
    films      = models.ForeignKey(Film, on_delete=models.CASCADE)
    users      = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

class CommentLike(models.Model):
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE)
    users    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments_likes'

class Reply(TimeStampModel):
    contents   = models.CharField(max_length=500)
    deleted_at = models.DateTimeField()
    comments   = models.ForeignKey('Comment', on_delete=models.CASCADE)
    users      = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'replies'
