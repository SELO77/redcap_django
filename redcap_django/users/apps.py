from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "redcap_django.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import redcap_django.users.signals  # noqa F401
        except ImportError:
            pass
