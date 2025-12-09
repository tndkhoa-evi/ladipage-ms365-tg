"""
Vercel serverless handler for Django.
"""
import os
import sys

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django BEFORE importing WSGI application
import django
django.setup()

from django.core.wsgi import get_wsgi_application

app = application = get_wsgi_application()
