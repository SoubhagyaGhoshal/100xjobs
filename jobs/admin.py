from django.contrib import admin
from .models import Company, Category, Job, Application, SavedJob, Testimonial, FAQ


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "employment_type", "work_mode", "is_active", "created_at")
    list_filter = ("company", "category", "employment_type", "work_mode", "experience_level", "is_active", "created_at")
    search_fields = ("title", "description", "location", "skills_required")
    list_editable = ("is_active",)
    date_hierarchy = "created_at"
    
    fieldsets = (
        ("Basic Information", {
            "fields": ("title", "description", "company", "category", "posted_by")
        }),
        ("Job Details", {
            "fields": ("employment_type", "work_mode", "experience_level", "location")
        }),
        ("Requirements & Skills", {
            "fields": ("requirements", "responsibilities", "skills_required")
        }),
        ("Compensation", {
            "fields": ("salary_min", "salary_max", "salary_currency")
        }),
        ("Settings", {
            "fields": ("is_active", "application_deadline")
        }),
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "applicant", "status", "created_at")
    list_filter = ("status", "created_at", "job__company")
    search_fields = ("job__title", "applicant__username", "applicant__email")
    list_editable = ("status",)
    date_hierarchy = "created_at"


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ("user", "job", "created_at")
    list_filter = ("created_at", "job__company")
    search_fields = ("user__username", "job__title")
    date_hierarchy = "created_at"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "rating", "is_active", "created_at")
    list_filter = ("rating", "is_active", "created_at")
    search_fields = ("name", "company", "content")
    list_editable = ("is_active",)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("question", "answer")
    list_editable = ("order", "is_active")
    ordering = ("order", "-created_at")
