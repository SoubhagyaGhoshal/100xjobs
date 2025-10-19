#!/bin/bash

echo "🚀 Starting Render build process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Run debug script to see what's happening
echo "🔍 Running debug diagnostics..."
python debug_build.py

# Simple, direct migration approach
echo "🗄️ Running Django migrations..."

# First, ensure Django can connect to database
echo "🔗 Testing database connection..."
python -c "
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()
from django.db import connection
print('Testing database connection...')
with connection.cursor() as cursor:
    cursor.execute('SELECT version()')
    print(f'Connected to: {cursor.fetchone()[0]}')
"

# Create migrations
echo "📝 Making migrations..."
python manage.py makemigrations
python manage.py makemigrations jobs
python manage.py makemigrations accounts

# Apply migrations
echo "🔄 Applying migrations..."
python manage.py migrate

# Verify tables were created
echo "📋 Verifying tables..."
python -c "
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute(\"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name\")
    tables = [row[0] for row in cursor.fetchall()]
    print(f'Tables created: {tables}')
    if 'jobs_job' in tables:
        print('✅ Job tables created successfully')
    else:
        print('❌ Job tables missing')
        raise Exception('Migration failed - no job tables')
"

# Create superuser
echo "👤 Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Superuser created: admin/admin123')
else:
    print('✅ Superuser already exists')
"

# Populate sample data
echo "🎯 Populating sample data..."
python manage.py populate_sample_data || echo "⚠️ Sample data population failed"

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✅ Build completed successfully!"
