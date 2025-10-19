#!/bin/bash

set -o errexit  # Exit on error

echo "🚀 Starting Render build process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create superuser if it doesn't exist (optional)
echo "👤 Creating superuser (if needed)..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
" || echo "Superuser creation skipped"

# Populate sample data (optional - only if tables are empty)
echo "🎯 Populating sample data (if needed)..."
python manage.py shell -c "
from jobs.models import Job
if Job.objects.count() == 0:
    import os
    os.system('python manage.py populate_sample_data')
    print('Sample data populated')
else:
    print('Sample data already exists')
" || echo "Sample data population skipped"

echo "✅ Build completed successfully!"
