from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

# https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/
class Command(BaseCommand):

    def handle(self, *args, **options):
        print("*** Start to create superuser(ROOT ADMIN).")
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser('admin', "admin@admin.com", "qwer1234")
            print("**** Superuser has been created.")
        else:
            print("**** Superuser is already existed.")

