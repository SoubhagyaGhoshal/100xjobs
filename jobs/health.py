from django.http import JsonResponse
from django.db import connection
from jobs.models import Job, Company, Category
import os


def health_check(request):
    """Health check endpoint to diagnose deployment issues"""
    status = {
        'status': 'ok',
        'database': 'unknown',
        'tables': [],
        'environment': {},
        'errors': []
    }
    
    # Check environment variables
    status['environment'] = {
        'DATABASE_URL': 'set' if os.environ.get('DATABASE_URL') else 'not set',
        'DEBUG': os.environ.get('DEBUG', 'not set'),
        'ALLOWED_HOSTS': os.environ.get('ALLOWED_HOSTS', 'not set'),
    }
    
    # Check database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version()")
            version = cursor.fetchone()[0]
            status['database'] = f'connected: {version[:50]}'
    except Exception as e:
        status['database'] = f'error: {str(e)}'
        status['errors'].append(f'Database connection: {str(e)}')
        status['status'] = 'error'
    
    # Check if tables exist
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            tables = cursor.fetchall()
            status['tables'] = [t[0] for t in tables]
    except Exception as e:
        status['errors'].append(f'Table listing: {str(e)}')
    
    # Check if models work
    try:
        job_count = Job.objects.count()
        status['job_count'] = job_count
    except Exception as e:
        status['errors'].append(f'Job model: {str(e)}')
        status['status'] = 'error'
    
    try:
        company_count = Company.objects.count()
        status['company_count'] = company_count
    except Exception as e:
        status['errors'].append(f'Company model: {str(e)}')
    
    return JsonResponse(status, json_dumps_params={'indent': 2})
