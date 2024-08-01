import os
from django.core.wsgi import get_wsgi_application
import dj_database_url

from ts_v5_settings.settings import DATABASES

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ts_v5_project.settings')  # Replace with your project name

application = get_wsgi_application()

# Heroku Database Configuration
db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES['default'].update(db_from_env)
