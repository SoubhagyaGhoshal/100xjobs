#!/usr/bin/env python
"""
Debug script to check what's happening during build
"""
import os
import sys

print("🔍 DEBUG BUILD SCRIPT")
print("=" * 50)

# Check environment
print("📋 Environment Variables:")
for key in ['DATABASE_URL', 'DEBUG', 'ALLOWED_HOSTS', 'SECRET_KEY']:
    value = os.environ.get(key, 'NOT SET')
    if key == 'DATABASE_URL' and value != 'NOT SET':
        # Mask password in URL
        if '@' in value:
            parts = value.split('@')
            masked = parts[0].split(':')[:-1] + ['***'] + ['@'] + parts[1:]
            value = ':'.join(masked[:-2]) + ''.join(masked[-2:])
    print(f"  {key}: {value}")

print("\n📁 Current Directory:")
print(f"  {os.getcwd()}")

print("\n📂 Files in current directory:")
for item in sorted(os.listdir('.')):
    if os.path.isfile(item):
        size = os.path.getsize(item)
        print(f"  📄 {item} ({size} bytes)")
    else:
        print(f"  📁 {item}/")

print("\n🐍 Python Path:")
for path in sys.path[:5]:  # Show first 5 paths
    print(f"  {path}")

print("\n🔧 Django Setup Test:")
try:
    import django
    print(f"  Django version: {django.get_version()}")
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
    django.setup()
    print("  ✅ Django setup successful")
    
    from django.db import connection
    print("  🔗 Testing database connection...")
    with connection.cursor() as cursor:
        cursor.execute("SELECT version()")
        version = cursor.fetchone()[0]
        print(f"  ✅ Database connected: {version[:50]}...")
        
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
        """)
        tables = [row[0] for row in cursor.fetchall()]
        print(f"  📋 Tables in database: {len(tables)}")
        for table in tables[:10]:  # Show first 10 tables
            print(f"    - {table}")
        if len(tables) > 10:
            print(f"    ... and {len(tables) - 10} more")
            
except Exception as e:
    print(f"  ❌ Django setup failed: {e}")

print("\n" + "=" * 50)
print("🔍 DEBUG BUILD SCRIPT COMPLETE")
