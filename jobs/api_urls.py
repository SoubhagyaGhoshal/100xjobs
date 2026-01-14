from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobs.api_views import JobViewSet, CompanyViewSet, CategoryViewSet, TestimonialViewSet, FAQViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'faqs', FAQViewSet, basename='faq')

urlpatterns = [
    path('', include(router.urls)),
]
