from django.core.signing import Signer

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    signer = Signer()

    email_verification_link = models.CharField(
        null=True,
        max_length=1024
    )
    is_email_verified = models.BooleanField(default=False)
    verification_email_sent_at = models.DateTimeField(null=True)
    incorrect_attempts = models.PositiveSmallIntegerField(default=0)
    is_seller = models.BooleanField(default=False)
    initial_secret_key = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    man = models.BooleanField(default=False)
    woman = models.BooleanField(default=False)
    birth = models.DateTimeField(null=True)
    number_phone = models.CharField(max_length=256, null=True)
