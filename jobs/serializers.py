from rest_framework import serializers
from .models import Job, Company, Category, Application, SavedJob, Testimonial, FAQ


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class JobSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    skills = serializers.SerializerMethodField()
    salary = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    posted_date = serializers.SerializerMethodField()
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'requirements', 'responsibilities',
            'company', 'category', 'location', 'employment_type', 'work_mode',
            'experience', 'salary', 'skills', 'is_active', 'posted_date',
            'application_deadline'
        ]
    
    def get_skills(self, obj):
        return obj.skills_list
    
    def get_salary(self, obj):
        if obj.salary_min and obj.salary_max:
            return f"{obj.salary_min//1000}K-{obj.salary_max//1000}K"
        elif obj.salary_min:
            return f"{obj.salary_min//1000}K+"
        return "Not specified"
    
    def get_experience(self, obj):
        experience_map = {
            'entry': '0-1 Yrs',
            'junior': '1-3 Yrs',
            'mid': '3-5 Yrs',
            'senior': '5-8 Yrs',
            'lead': '8+ Yrs',
        }
        return experience_map.get(obj.experience_level, obj.get_experience_level_display())
    
    def get_posted_date(self, obj):
        return obj.created_at.strftime('%a %b %d %Y')


class JobListSerializer(serializers.ModelSerializer):
    """Simplified serializer for job listings"""
    company_name = serializers.CharField(source='company.name', read_only=True)
    skills = serializers.SerializerMethodField()
    salary = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    posted_date = serializers.SerializerMethodField()
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'company_name', 'location', 'employment_type',
            'work_mode', 'experience', 'salary', 'skills', 'posted_date'
        ]
    
    def get_skills(self, obj):
        return obj.skills_list[:6]  # Limit to 6 skills for list view
    
    def get_salary(self, obj):
        if obj.salary_min and obj.salary_max:
            return f"{obj.salary_min//1000}K-{obj.salary_max//1000}K"
        return "Not specified"
    
    def get_experience(self, obj):
        experience_map = {
            'entry': '0-1 Yrs',
            'junior': '1-3 Yrs',
            'mid': '3-5 Yrs',
            'senior': '5-8 Yrs',
            'lead': '8+ Yrs',
        }
        return experience_map.get(obj.experience_level, obj.get_experience_level_display())
    
    def get_posted_date(self, obj):
        return obj.created_at.strftime('%a %b %d %Y')


class ApplicationSerializer(serializers.ModelSerializer):
    job = JobListSerializer(read_only=True)
    applicant_name = serializers.CharField(source='applicant.username', read_only=True)
    
    class Meta:
        model = Application
        fields = ['id', 'job', 'applicant_name', 'cover_letter', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'position', 'company', 'content', 'rating']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'order']
