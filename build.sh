#!/bin/bash

set -o errexit  # Exit on error

echo "🚀 Starting Render build process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Set up database with comprehensive error handling
echo "🔧 Setting up database..."
python manage.py setup_database

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✅ Build completed successfully!"
