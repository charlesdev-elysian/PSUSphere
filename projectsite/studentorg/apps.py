from django.apps import AppConfig

class StudentorgConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studentorg'  # ✅ Make sure it matches the folder name exactly
