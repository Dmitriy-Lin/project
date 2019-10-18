import random
import string
import base64
import urllib

from datetime import timedelta
from django.core.signing import TimestampSigner

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

ALPHABET = (string.digits + string.ascii_letters + string.punctuation) * 50


class User(AbstractUser):
    signer = TimestampSigner(salt='Friends')

    email_verification_link = models.CharField(
        null=True,
        max_length=1024
    )
    is_email_verified = models.BooleanField(default=False)
    verification_email_sent_at = models.DateTimeField(null=True)
    incorrect_attempts = models.PositiveSmallIntegerField(default=0)
    initial_secret_key = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    man = models.BooleanField(default=False)
    woman = models.BooleanField(default=False)
    birth = models.DateTimeField(null=True)
    number_phone = models.CharField(max_length=256, null=True)
    avatar = models.ImageField(upload_to="img/", default="img/none.jpg")

    def generate_key(self):
        key = "".join(
            random.sample(ALPHABET, 256)
        )
        self.initial_secret_key = key
        self.save()

        signed_key = self.signer.sign(key)
        encoded_key = base64.b64encode(bytes(signed_key, encoding='ascii')).decode('utf-8')
        return encoded_key

    def verify_email(self):
        encoded_key = self.generate_key()
        url = "http://127.0.0.1:8000/verify?key={}".format(
            urllib.parse.quote(encoded_key)
        )
        self.verification_email_sent_at = timezone.now()
        self.save()
        self.email_user(
            "Verification Link",
            "<a href={}>".format(url),
            "admin@friends.com"
        )

    def check_key(self, key):
        signed_key = base64.b64decode(key).decode('utf-8')
        initial_key = self.signer.unsign(signed_key, max_age=timedelta(days=1))
        return self.initial_secret_key == initial_key
