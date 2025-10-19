#!/usr/bin/env python3
"""
Python build script for Render deployment
More reliable than bash script
"""

import os
import sys
import subprocess
import django

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def main():
    print("🚀 Starting Python build process...")
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
    
    # Test Django setup
    print("🔧 Setting up Django...")
    try:
        django.setup()
        print("✅ Django setup successful")
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False
    
    # Test database connection
    print("🔗 Testing database connection...")
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT version()")
            version = cursor.fetchone()[0]
            print(f"✅ Connected to: {version[:50]}...")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False
    
    # Check current tables
    print("📋 Checking existing tables...")
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            tables = [row[0] for row in cursor.fetchall()]
            print(f"📋 Found {len(tables)} tables: {tables[:5]}{'...' if len(tables) > 5 else ''}")
    except Exception as e:
        print(f"⚠️ Could not list tables: {e}")
    
    # Run migrations
    print("🗄️ Running migrations...")
    from django.core.management import call_command
    
    try:
        # Make migrations
        print("📝 Creating migrations...")
        call_command('makemigrations', verbosity=1, interactive=False)
        call_command('makemigrations', 'jobs', verbosity=1, interactive=False)
        call_command('makemigrations', 'accounts', verbosity=1, interactive=False)
        
        # Apply migrations
        print("🔄 Applying migrations...")
        call_command('migrate', verbosity=1, interactive=False)
        
        print("✅ Migrations completed successfully")
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False
    
    # Verify tables were created
    print("📋 Verifying tables after migration...")
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)
            tables = [row[0] for row in cursor.fetchall()]
            print(f"📋 Now have {len(tables)} tables")
            
            # Check for job tables specifically
            job_tables = [t for t in tables if 'job' in t.lower()]
            if job_tables:
                print(f"✅ Job tables created: {job_tables}")
            else:
                print("❌ No job tables found!")
                return False
                
    except Exception as e:
        print(f"❌ Table verification failed: {e}")
        return False
    
    # Create superuser
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
        print(f"⚠️ Superuser creation failed: {e}")
    
    # Populate sample data
    print("🎯 Populating sample data...")
    try:
        call_command('populate_sample_data')
        print("✅ Sample data populated")
    except Exception as e:
        print(f"⚠️ Sample data population failed: {e}")
    
    # Collect static files
    print("📁 Collecting static files...")
    try:
        call_command('collectstatic', verbosity=1, interactive=False, clear=True)
        print("✅ Static files collected")
    except Exception as e:
        print(f"❌ Static file collection failed: {e}")
        return False
    
    print("🎉 Build completed successfully!")
    return True

if __name__ == '__main__':
    success = main()
    if not success:
        sys.exit(1)
