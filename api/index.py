import os
import sys
from pathlib import Path

# Add the project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')

# Import Django
import django
from django.core.wsgi import get_wsgi_application

# Configure Django
django.setup()

# Get WSGI application
application = get_wsgi_application()

# Vercel handler function
def handler(request):
    return application(request, {})
