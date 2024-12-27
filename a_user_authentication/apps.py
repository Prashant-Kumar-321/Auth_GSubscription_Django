from django.apps import AppConfig


class AUserAuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'a_user_authentication'

    def ready(self): 
        import a_user_authentication.signals
