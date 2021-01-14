from django.core.management.base import BaseCommand
from django.utils import timezone

import secrets

secret_key = secrets.token_urlsafe()

class Command(BaseCommand):
    help = 'Displays a new secret key'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(secret_key))
