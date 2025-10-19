#!/bin/bash

set -o errexit  # Exit on error

echo "🚀 Starting Render build process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Force database migrations first
echo "🔧 Force migrating database..."
python manage.py force_migrate

# Set up database with comprehensive error handling
echo "🔧 Setting up database..."
python manage.py setup_database || echo "⚠️ Setup database had issues, continuing..."

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✅ Build completed successfully!"
