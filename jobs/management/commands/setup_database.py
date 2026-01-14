from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.db import connection


class Command(BaseCommand):
    help = 'Set up database with migrations and initial data'

    def handle(self, *args, **options):
        self.stdout.write('🔧 Setting up database...')
        
        # Check database connection
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            self.stdout.write(self.style.SUCCESS('✅ Database connection successful'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Database connection failed: {e}'))
            return
        
        # Run migrations
        self.stdout.write('🗄️ Running migrations...')
        try:
            call_command('makemigrations', verbosity=1, interactive=False)
            call_command('migrate', verbosity=1, interactive=False)
            self.stdout.write(self.style.SUCCESS('✅ Migrations completed'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Migration failed: {e}'))
            return
        
        # Create superuser
        self.stdout.write('👤 Creating superuser...')
        try:
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
                self.stdout.write(self.style.SUCCESS('✅ Superuser created: admin/admin123'))
            else:
                self.stdout.write(self.style.WARNING('⚠️ Superuser already exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Superuser creation failed: {e}'))
        
        # Populate sample data
        self.stdout.write('🎯 Populating sample data...')
        try:
            from jobs.models import Job
            if Job.objects.count() == 0:
                call_command('populate_sample_data')
                self.stdout.write(self.style.SUCCESS('✅ Sample data populated'))
            else:
                self.stdout.write(self.style.WARNING('⚠️ Sample data already exists'))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'⚠️ Sample data population skipped: {e}'))
        
        self.stdout.write(self.style.SUCCESS('🎉 Database setup completed!'))
