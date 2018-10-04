from django.core.management.base import BaseCommand, CommandError
from users.models import Users

class Command(BaseCommand):
    help = 'Reset the status for all the dispatchers'

    def handle(self, *args, **options):
        for code in range(1,5):
            u=Users.objects.get(code=code)
            #print(u.name,u.active)
            u.active=True
            #print(u.name,u.active)
            u.save()