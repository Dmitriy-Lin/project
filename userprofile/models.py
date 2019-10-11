from django.db import models

from registration.models import User


class Post(models.Model):

    created = models.DateTimeField(auto_now=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey(
        User,
        related_name ='posts',
        on_delete = models.DO_NOTHING
    )


class Friends(models.Model):

    owner = models.ForeignKey(
        User,
        related_name ='owner_friends',
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name ='user_friends',
        on_delete = models.CASCADE
    )
    confirm = models.BooleanField(default=False)
