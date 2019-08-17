from django.conf import settings
from django.db import models


class Puzzle(models.Model):
    url = models.URLField()
    title = models.TextField()
    description = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # link = models.ForeignKey('puzzles.Link', related_name='votes', on_delete=models.CASCADE)

