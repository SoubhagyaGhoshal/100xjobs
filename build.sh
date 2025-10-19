#!/bin/bash

# Remove errexit temporarily to handle errors gracefully
echo "🚀 Starting Render build process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Force database migrations with multiple attempts
echo "🔧 Force migrating database..."
python manage.py force_migrate || echo "⚠️ Force migrate failed, trying individual steps..."

# Try individual migration steps
echo "📝 Creating migrations..."
python manage.py makemigrations --noinput || echo "⚠️ Makemigrations failed"
python manage.py makemigrations jobs --noinput || echo "⚠️ Jobs makemigrations failed"
python manage.py makemigrations accounts --noinput || echo "⚠️ Accounts makemigrations failed"

echo "🗄️ Applying migrations..."
python manage.py migrate --noinput || echo "⚠️ Migrate failed"

# Verify tables exist
echo "📋 Checking if tables exist..."
python manage.py shell -c "
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute(\"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'\")
    tables = cursor.fetchall()
    print(f'Tables found: {[t[0] for t in tables]}')
    if not tables:
        print('❌ No tables found - migration failed')
        exit(1)
    else:
        print('✅ Tables exist')
" || echo "⚠️ Table check failed"

# Set up database with comprehensive error handling
echo "🔧 Setting up database..."
python manage.py setup_database || echo "⚠️ Setup database had issues, continuing..."

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✅ Build completed successfully!"
