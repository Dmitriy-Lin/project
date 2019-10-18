from django.db import models

from registration.models import User


class Post(models.Model):

    created = models.DateTimeField(auto_now=True)
    body = models.TextField(blank=True)
    media = models.ImageField(upload_to="img/", blank=True, null=True)
    owner = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.DO_NOTHING
    )


class CommentPost(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='owner_comment',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='user_comment',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now=True)
    body = models.TextField(blank=True)


class Friends(models.Model):

    owner = models.ForeignKey(
        User,
        related_name='owner_friends',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='user_friends',
        on_delete=models.CASCADE
    )
    confirm = models.BooleanField(default=False)


class UserPhoto(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_photo',
        on_delete=models.CASCADE
    )
    desc = models.CharField(max_length=256, null=True)
    photo = models.ImageField(upload_to="img/", null=True)
