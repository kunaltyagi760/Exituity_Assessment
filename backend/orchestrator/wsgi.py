import os
from django.core.wsgi import get_wsgi_application

# Set default settings module for 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orchestrator.settings')

# Get the WSGI application for the project
application = get_wsgi_application()
