from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job, Company, Category, Application, Testimonial, FAQ
from .serializers import (
    JobSerializer, JobListSerializer, CompanySerializer,
    CategorySerializer, ApplicationSerializer, TestimonialSerializer, FAQSerializer
)


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for jobs
    GET /api/jobs/ - List all jobs
    GET /api/jobs/{id}/ - Get job detail
    """
    queryset = Job.objects.filter(is_active=True).select_related('company', 'category')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employment_type', 'work_mode', 'experience_level', 'location']
    search_fields = ['title', 'description', 'company__name']
    ordering_fields = ['created_at', 'salary_min']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return JobListSerializer
        return JobSerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for companies
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for testimonials
    """
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer


class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for FAQs
    """
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer
