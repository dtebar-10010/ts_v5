from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Resets the password for a given Django admin user.'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = input('Enter the admin username: ').strip()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'User "{username}" does not exist.'))
            return

        new_password = input('Enter the new password: ').strip()
        if not new_password:
            self.stderr.write(self.style.ERROR('Password cannot be empty.'))
            return

        user.set_password(new_password)
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Password successfully updated for user "{username}".'))
