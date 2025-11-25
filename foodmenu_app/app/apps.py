from django.apps import AppConfig


class AppConfigReal(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
