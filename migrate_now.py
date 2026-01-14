#!/usr/bin/env python
"""
Simple migration script that can be run manually in Render shell
Usage: python migrate_now.py
"""

import os
import django
from django.core.management import execute_from_command_line

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from django.db import connection
from django.core.management import call_command

def main():
    print("🚀 Manual migration script starting...")
    
    # Test database connection
    print("🔗 Testing database connection...")
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT version()")
            version = cursor.fetchone()[0]
            print(f"✅ Connected to: {version}")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False
    
    # Show current tables
    print("📋 Current tables:")
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            tables = [row[0] for row in cursor.fetchall()]
            print(f"Tables: {tables}")
    except Exception as e:
        print(f"❌ Could not list tables: {e}")
    
    # Run migrations
    print("🗄️ Running migrations...")
    try:
        call_command('migrate', verbosity=2, interactive=False)
        print("✅ Migrations completed")
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    # Verify tables were created
    print("📋 Verifying tables after migration:")
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            tables = [row[0] for row in cursor.fetchall()]
            print(f"Tables after migration: {tables}")
            
            # Check for specific tables
            job_tables = [t for t in tables if 'job' in t.lower()]
            if job_tables:
                print(f"✅ Job tables found: {job_tables}")
            else:
                print("❌ No job tables found")
                return False
                
    except Exception as e:
        print(f"❌ Table verification failed: {e}")
        return False
    
    # Create superuser if needed
    print("👤 Creating superuser...")
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print("✅ Superuser created: admin/admin123")
        else:
            print("✅ Superuser already exists")
    except Exception as e:
        print(f"❌ Superuser creation failed: {e}")
    
    print("🎉 Migration script completed successfully!")
    return True

if __name__ == '__main__':
    success = main()
    if not success:
        exit(1)
