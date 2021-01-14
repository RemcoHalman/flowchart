from django.core.management.base import BaseCommand
from django.utils import timezone

from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone

now_utc = datetime.now(timezone('UTC'))
now_local = now_utc.astimezone(get_localzone())

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = now_local.strftime('%X')
        self.stdout.write(self.style.SUCCESS("\nIt's now %s\n" % time))
