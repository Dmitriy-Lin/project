import json
import os
from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand
from django.conf import settings

from registration.models import User


SEED_FILE = os.path.join(
    settings.BASE_DIR,
    'static',
    'friends.json'
)


class Command(BaseCommand):
    help = 'Populates the database with seed data'

    def add_arguments(self, parser):
        parser.add_argument('--truncate', '-t', default=False, action='store_true')

    def handle(self, *args, **options):
        if options['truncate']:
            User.objects.all().delete()

        with open(SEED_FILE) as f:
            friends = json.load(f)

        bulk_friend = []
        for friend in friends:
            bulk_friend.append(
                User(
                    username=friend['domain'],
                    email='52kage@mail.ru',
                    password=make_password('52412630aA'),
                    first_name=friend['first_name'],
                    last_name=friend['last_name'],
                    city=friend['city'],
                    country='Беларусь',
                    number_phone=friend['id'],
                    avatar=friend['img']
                )
            )
            self.stdout.write(f"Friends {friend['first_name']} processed")

        User.objects.bulk_create(bulk_friend)
