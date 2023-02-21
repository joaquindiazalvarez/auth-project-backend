from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration of the authApp app
    Defines size of id field(big integer) on app model with default_auto_field
    Defines the name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authApp'
