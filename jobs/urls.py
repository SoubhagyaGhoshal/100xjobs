from django.urls import path
from . import views
from .health import health_check

app_name = "jobs"

urlpatterns = [
    path("", views.home, name="home"),
    path("health/", health_check, name="health_check"),
    path("jobs/<int:pk>/", views.job_detail, name="job_detail"),
    path("jobs/create/", views.job_create, name="job_create"),
    path("jobs/<int:pk>/edit/", views.job_edit, name="job_edit"),
    path("jobs/<int:pk>/delete/", views.job_delete, name="job_delete"),
    path("jobs/<int:pk>/apply/", views.apply_job, name="apply_job"),
    path("jobs/<int:pk>/save/", views.save_job, name="save_job"),
    path("jobs/<int:pk>/unsave/", views.unsave_job, name="unsave_job"),
    path("saved-jobs/", views.saved_jobs, name="saved_jobs"),
    path("my-applications/", views.my_applications, name="my_applications"),
    path("employer/dashboard/", views.employer_dashboard, name="employer_dashboard"),
    path("jobs/<int:pk>/applications/", views.job_applications, name="job_applications"),
    path("applications/<int:pk>/update-status/", views.update_application_status, name="update_application_status"),
]
