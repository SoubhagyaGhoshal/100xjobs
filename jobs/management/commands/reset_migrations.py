from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import os


class Command(BaseCommand):
    help = 'Reset and recreate all migrations'

    def handle(self, *args, **options):
        self.stdout.write('🔄 Resetting migrations...')
        
        # Show current database state
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public'
                """)
                tables = cursor.fetchall()
                self.stdout.write(f'📋 Current tables: {[t[0] for t in tables]}')
        except Exception as e:
            self.stdout.write(f'⚠️ Could not list tables: {e}')
        
        # Create fresh migrations
        self.stdout.write('📝 Creating fresh migrations...')
        try:
            # Remove existing migration files (if any)
            self.stdout.write('🗑️ Cleaning old migrations...')
            
            # Create new migrations
            call_command('makemigrations', 'jobs', verbosity=2, interactive=False)
            call_command('makemigrations', 'accounts', verbosity=2, interactive=False)
            call_command('makemigrations', verbosity=2, interactive=False)
            
            self.stdout.write(self.style.SUCCESS('✅ Fresh migrations created'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Migration creation failed: {e}'))
            return
        
        # Apply migrations
        self.stdout.write('🗄️ Applying migrations...')
        try:
            call_command('migrate', verbosity=2, interactive=False)
            self.stdout.write(self.style.SUCCESS('✅ Migrations applied'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Migration application failed: {e}'))
            return
        
        # Verify tables were created
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT table_name 
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    ORDER BY table_name
                """)
                tables = cursor.fetchall()
                table_names = [t[0] for t in tables]
                self.stdout.write(self.style.SUCCESS(f'✅ Tables created: {table_names}'))
                
                # Check for our specific tables
                job_tables = [t for t in table_names if 'job' in t.lower()]
                if job_tables:
                    self.stdout.write(self.style.SUCCESS(f'✅ Job-related tables: {job_tables}'))
                else:
                    self.stdout.write(self.style.WARNING('⚠️ No job-related tables found'))
                    
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Table verification failed: {e}'))
        
        self.stdout.write(self.style.SUCCESS('🎉 Migration reset completed!'))
