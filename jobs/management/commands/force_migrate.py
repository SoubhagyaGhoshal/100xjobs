from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import os


class Command(BaseCommand):
    help = 'Force database migrations and setup'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Force migrating database...')
        
        # Show current environment
        self.stdout.write(f'DATABASE_URL: {os.environ.get("DATABASE_URL", "Not set")}')
        
        # Test database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT version()")
                version = cursor.fetchone()[0]
                self.stdout.write(self.style.SUCCESS(f'✅ Connected to: {version}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Database connection failed: {e}'))
            return
        
        # Show existing tables
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                tables = cursor.fetchall()
                self.stdout.write(f'📋 Existing tables: {[t[0] for t in tables]}')
        except Exception as e:
            self.stdout.write(f'⚠️ Could not list tables: {e}')
        
        # Force make migrations
        self.stdout.write('📝 Creating migrations...')
        try:
            call_command('makemigrations', 'jobs', verbosity=2, interactive=False)
            call_command('makemigrations', 'accounts', verbosity=2, interactive=False)
            call_command('makemigrations', verbosity=2, interactive=False)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'⚠️ Makemigrations warning: {e}'))
        
        # Force migrate
        self.stdout.write('🗄️ Applying migrations...')
        try:
            call_command('migrate', verbosity=2, interactive=False)
            self.stdout.write(self.style.SUCCESS('✅ Migrations applied successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Migration failed: {e}'))
            return
        
        # Verify tables exist
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' AND table_name LIKE '%job%'
                """)
                job_tables = cursor.fetchall()
                self.stdout.write(self.style.SUCCESS(f'✅ Job tables created: {[t[0] for t in job_tables]}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Could not verify tables: {e}'))
        
        self.stdout.write(self.style.SUCCESS('🎉 Force migration completed!'))
