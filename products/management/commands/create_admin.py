from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        username = config("DJANGO_SUPERUSER_USERNAME", "admin")
        email = config("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        password = config("DJANGO_SUPERUSER_PASSWORD", "password")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists'))
