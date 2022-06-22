from django.db import models

from films.models import Film
from users.models import User
from core.models  import TimeStampModel

class Comment(TimeStampModel):
    content    = models.CharField(max_length=500)
    deleted_at = models.DateTimeField(null=True)
    film       = models.ForeignKey(Film, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'

class CommentLike(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'comments_likes'

class Reply(TimeStampModel):
    content    = models.CharField(max_length=500)
    deleted_at = models.DateTimeField(null=True)
    comment    = models.ForeignKey('Comment', on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'replies'
