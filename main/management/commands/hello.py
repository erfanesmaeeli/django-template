from django.core.management.base import BaseCommand, no_translations


class Command(BaseCommand):

    @no_translations
    def handle(self, *args, **options):
        print("hello world!")