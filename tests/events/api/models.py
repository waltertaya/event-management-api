from django.db import models


class RSVP(models.Model):
    user_id = models.IntegerField()
    event_id = models.IntegerField()


class Comment(models.Model):
    user_id = models.IntegerField()
    event_id = models.IntegerField()
    text = models.TextField()
