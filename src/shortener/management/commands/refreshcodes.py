from django.core.management.base import BaseCommand, CommandError
from shortener.models import URL


# python3 manage.py refreshcodes

class Command(BaseCommand):
    help = 'Refresh all URL shortcode'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return URL.objects.refresh_shortcodes()