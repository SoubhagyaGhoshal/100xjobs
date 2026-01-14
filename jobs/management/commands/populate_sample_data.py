from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from jobs.models import Company, Category, Job, Testimonial, FAQ
from accounts.models import UserProfile
import random
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create companies
        companies_data = [
            'Google', 'Microsoft', 'Apple', 'Amazon', 'Meta', 'Netflix', 'Tesla',
            'Uber', 'Airbnb', 'Stripe', 'Spotify', 'Twitter', 'LinkedIn', 'Adobe',
            'Salesforce', 'Oracle', 'IBM', 'Intel', 'NVIDIA', 'PayPal'
        ]
        
        companies = []
        for company_name in companies_data:
            company, created = Company.objects.get_or_create(name=company_name)
            companies.append(company)
            if created:
                self.stdout.write(f'Created company: {company_name}')

        # Create categories
        categories_data = [
            ('Software Engineering', 'software-engineering'),
            ('Data Science', 'data-science'),
            ('Product Management', 'product-management'),
            ('Design', 'design'),
            ('Marketing', 'marketing'),
            ('Sales', 'sales'),
            ('DevOps', 'devops'),
            ('Mobile Development', 'mobile-development'),
            ('Frontend Development', 'frontend-development'),
            ('Backend Development', 'backend-development'),
        ]
        
        categories = []
        for name, slug in categories_data:
            category, created = Category.objects.get_or_create(name=name, slug=slug)
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {name}')

        # Create sample employer users
        employers = []
        for i in range(5):
            username = f'employer{i+1}'
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': f'{username}@example.com',
                    'first_name': f'Employer',
                    'last_name': f'{i+1}',
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                user.profile.role = 'employer'
                user.profile.company_name = random.choice(companies).name
                user.profile.save()
                employers.append(user)
                self.stdout.write(f'Created employer: {username}')

        # Create sample job seeker users
        job_seekers = []
        for i in range(10):
            username = f'jobseeker{i+1}'
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': f'{username}@example.com',
                    'first_name': f'Job',
                    'last_name': f'Seeker{i+1}',
                }
            )
            if created:
                user.set_password('password123')
                user.save()
                user.profile.role = 'job_seeker'
                user.profile.location = random.choice(['New York', 'San Francisco', 'London', 'Berlin', 'Toronto'])
                user.profile.bio = f'Experienced professional looking for new opportunities in tech.'
                user.profile.save()
                job_seekers.append(user)
                self.stdout.write(f'Created job seeker: {username}')

        # Create sample jobs
        job_titles = [
            'Senior Software Engineer', 'Frontend Developer', 'Backend Developer',
            'Full Stack Developer', 'Data Scientist', 'Product Manager',
            'UX Designer', 'DevOps Engineer', 'Mobile Developer',
            'Machine Learning Engineer', 'Software Architect', 'Technical Lead',
            'QA Engineer', 'Site Reliability Engineer', 'Security Engineer'
        ]

        skills_list = [
            'Python,Django,PostgreSQL', 'JavaScript,React,Node.js', 'Java,Spring,MySQL',
            'Python,Machine Learning,TensorFlow', 'AWS,Docker,Kubernetes',
            'React,TypeScript,GraphQL', 'Swift,iOS,Xcode', 'Android,Kotlin,Java',
            'Go,Microservices,Redis', 'C++,Algorithms,System Design'
        ]

        locations = ['New York, NY', 'San Francisco, CA', 'Seattle, WA', 'Austin, TX', 
                    'Boston, MA', 'London, UK', 'Berlin, Germany', 'Toronto, Canada']

        for i in range(50):
            title = random.choice(job_titles)
            company = random.choice(companies)
            category = random.choice(categories)
            employer = random.choice(employers) if employers else None
            
            if employer:
                job = Job.objects.create(
                    title=title,
                    description=f"We are looking for a talented {title.lower()} to join our team at {company.name}. "
                               f"You will be working on cutting-edge projects and collaborating with a world-class team.",
                    requirements=f"• 3+ years of experience in relevant technologies\n"
                               f"• Strong problem-solving skills\n"
                               f"• Experience with agile development\n"
                               f"• Excellent communication skills",
                    responsibilities=f"• Design and develop high-quality software solutions\n"
                                   f"• Collaborate with cross-functional teams\n"
                                   f"• Participate in code reviews and technical discussions\n"
                                   f"• Mentor junior developers",
                    salary_min=random.randint(80000, 120000),
                    salary_max=random.randint(120000, 200000),
                    salary_currency='USD',
                    location=random.choice(locations),
                    employment_type=random.choice(['full_time', 'part_time', 'contract']),
                    work_mode=random.choice(['remote', 'onsite', 'hybrid']),
                    experience_level=random.choice(['entry', 'junior', 'mid', 'senior']),
                    skills_required=random.choice(skills_list),
                    company=company,
                    category=category,
                    posted_by=employer,
                    is_active=True,
                    application_deadline=date.today() + timedelta(days=random.randint(30, 90))
                )
                self.stdout.write(f'Created job: {title} at {company.name}')

        # Create testimonials
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'position': 'Software Engineer',
                'company': 'Google',
                'content': '100xJobs helped me find my dream job at Google. The platform is user-friendly and has amazing job opportunities.',
                'rating': 5
            },
            {
                'name': 'Michael Chen',
                'position': 'Product Manager',
                'company': 'Microsoft',
                'content': 'As an employer, I\'ve found excellent candidates through 100xJobs. The quality of applicants is outstanding.',
                'rating': 5
            },
            {
                'name': 'Emily Davis',
                'position': 'UX Designer',
                'company': 'Apple',
                'content': 'The job search process was smooth and efficient. I received multiple offers within weeks of joining.',
                'rating': 4
            }
        ]

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(f'Created testimonial from: {testimonial_data["name"]}')

        # Create FAQs
        faqs_data = [
            {
                'question': 'How do I apply for jobs?',
                'answer': 'Simply create an account, browse available jobs, and click "Apply Now" on any job that interests you. You can upload your resume and write a cover letter.',
                'order': 1
            },
            {
                'question': 'Can I save jobs to apply for later?',
                'answer': 'Yes! Click the bookmark icon on any job listing to save it. You can view all your saved jobs in your dashboard.',
                'order': 2
            },
            {
                'question': 'Can I receive job alerts?',
                'answer': 'Job alerts are coming soon! You\'ll be able to set up custom alerts based on your preferences.',
                'order': 3
            },
            {
                'question': 'Is there a fee to use this job portal?',
                'answer': 'No, 100xJobs is completely free for job seekers. Employers pay a fee to post jobs.',
                'order': 4
            },
            {
                'question': 'Can I delete my account?',
                'answer': 'Yes, you can delete your account at any time from your account settings. This action is irreversible.',
                'order': 5
            },
            {
                'question': 'How do I create an account?',
                'answer': 'Click the "Register" button in the top navigation, fill out the form, and choose whether you\'re a job seeker or employer.',
                'order': 6
            }
        ]

        for faq_data in faqs_data:
            faq, created = FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults=faq_data
            )
            if created:
                self.stdout.write(f'Created FAQ: {faq_data["question"]}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
        self.stdout.write('You can now login with:')
        self.stdout.write('- Employers: employer1-5 / password123')
        self.stdout.write('- Job Seekers: jobseeker1-10 / password123')
