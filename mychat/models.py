from django.db import models

from registration.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, verbose_name="members")


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="chat", on_delete='CASCADE')
    author = models.ForeignKey(User, verbose_name="user", on_delete='CASCADE')
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
