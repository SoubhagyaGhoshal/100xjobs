from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.db import models
from django.core.paginator import Paginator
from .models import Job, Application, Company, Category, SavedJob, Testimonial, FAQ
from .forms import JobForm, ApplicationForm, JobSearchForm


def home(request):
    # Get search parameters
    q = request.GET.get("q", "")
    location = request.GET.get("location", "")
    category = request.GET.get("category", "")
    employment_type = request.GET.get("employment_type", "")
    work_mode = request.GET.get("work_mode", "")
    experience_level = request.GET.get("experience_level", "")
    salary_min = request.GET.get("salary_min", "")

    # Start with active jobs - with error handling for missing tables
    try:
        jobs = Job.objects.filter(is_active=True).select_related('company', 'category', 'posted_by')
    except Exception as e:
        # If tables don't exist, return empty queryset and show setup message
        from django.http import HttpResponse
        return HttpResponse("""
        <h1>Database Setup Required</h1>
        <p>The database tables haven't been created yet. This usually happens during the first deployment.</p>
        <p>Please wait a few minutes for the deployment to complete, then refresh this page.</p>
        <p>If this error persists, check the deployment logs in your Render dashboard.</p>
        <hr>
        <p><strong>Error:</strong> {}</p>
        """.format(str(e)))
    
    # Apply filters
    if q:
        jobs = jobs.filter(
            Q(title__icontains=q) | 
            Q(description__icontains=q) | 
            Q(company__name__icontains=q) |
            Q(skills_required__icontains=q)
        )
    if location:
        jobs = jobs.filter(location__icontains=location)
    if category:
        jobs = jobs.filter(category__slug=category)
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)
    if work_mode:
        jobs = jobs.filter(work_mode=work_mode)
    if experience_level:
        jobs = jobs.filter(experience_level=experience_level)
    if salary_min:
        try:
            salary_min = int(salary_min)
            jobs = jobs.filter(salary_min__gte=salary_min)
        except ValueError:
            pass

    # Pagination with error handling
    try:
        paginator = Paginator(jobs, 12)  # Show 12 jobs per page
        page_number = request.GET.get('page')
        jobs = paginator.get_page(page_number)

        categories = Category.objects.all()
        
        context = {
            "jobs": jobs,
            "categories": categories,
            "search_form": JobSearchForm(request.GET),
        }
        return render(request, "jobs/home.html", context)
    except Exception as e:
        # If pagination or categories fail due to missing tables
        from django.http import HttpResponse
        return HttpResponse(f"""
        <h1>Database Setup In Progress</h1>
        <p>The database is still being set up. Please wait a few minutes and refresh.</p>
        <p>If this error persists, the database migrations may not have run properly during deployment.</p>
        <hr>
        <p><strong>Technical Details:</strong></p>
        <p>Error: {str(e)}</p>
        <p>This usually means the database tables haven't been created yet.</p>
        <p><a href="/health/">Check System Health</a></p>
        """)


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    is_saved = False
    has_applied = False
    
    if request.user.is_authenticated:
        is_saved = SavedJob.objects.filter(user=request.user, job=job).exists()
        has_applied = Application.objects.filter(applicant=request.user, job=job).exists()
    
    context = {
        "job": job,
        "is_saved": is_saved,
        "has_applied": has_applied,
    }
    return render(request, "jobs/job_detail.html", context)


@login_required
def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, "Job posted")
            return redirect("jobs:job_detail", pk=job.pk)
    else:
        form = JobForm()
    return render(request, "jobs/job_form.html", {"form": form, "title": "Post Job"})


@login_required
def job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated")
            return redirect("jobs:job_detail", pk=job.pk)
    else:
        form = JobForm(instance=job)
    return render(request, "jobs/job_form.html", {"form": form, "title": "Edit Job"})


@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted")
        return redirect("jobs:home")
    return render(request, "jobs/job_confirm_delete.html", {"job": job})


@login_required
def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    
    # Check if user already applied
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.error(request, "You have already applied for this job")
        return redirect("jobs:job_detail", pk=job.pk)
    
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.applicant = request.user
            app.save()
            messages.success(request, "Applied successfully")
            return redirect("jobs:job_detail", pk=job.pk)
    else:
        form = ApplicationForm()
    return render(request, "jobs/apply_form.html", {"form": form, "job": job})


@login_required
def save_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    saved_job, created = SavedJob.objects.get_or_create(user=request.user, job=job)
    
    if created:
        messages.success(request, "Job saved successfully")
    else:
        messages.info(request, "Job already saved")
    
    return redirect("jobs:job_detail", pk=job.pk)


@login_required
def unsave_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    SavedJob.objects.filter(user=request.user, job=job).delete()
    messages.success(request, "Job removed from saved jobs")
    return redirect("jobs:job_detail", pk=job.pk)


@login_required
def saved_jobs(request):
    saved_jobs = SavedJob.objects.filter(user=request.user).select_related('job__company', 'job__category')
    paginator = Paginator(saved_jobs, 10)
    page_number = request.GET.get('page')
    saved_jobs = paginator.get_page(page_number)
    return render(request, "jobs/saved_jobs.html", {"saved_jobs": saved_jobs})


@login_required
def my_applications(request):
    applications = Application.objects.filter(applicant=request.user).select_related('job__company')
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    applications = paginator.get_page(page_number)
    return render(request, "jobs/my_applications.html", {"applications": applications})


@login_required
def employer_dashboard(request):
    if not request.user.profile.is_employer:
        messages.error(request, "Access denied. Employer account required.")
        return redirect("jobs:home")
    
    jobs = Job.objects.filter(posted_by=request.user).annotate(
        application_count=models.Count('applications')
    )
    recent_applications = Application.objects.filter(
        job__posted_by=request.user
    ).select_related('job', 'applicant')[:10]
    
    context = {
        'jobs': jobs,
        'recent_applications': recent_applications,
        'total_jobs': jobs.count(),
        'active_jobs': jobs.filter(is_active=True).count(),
        'total_applications': Application.objects.filter(job__posted_by=request.user).count(),
    }
    return render(request, "jobs/employer_dashboard.html", context)


@login_required
def job_applications(request, pk):
    job = get_object_or_404(Job, pk=pk, posted_by=request.user)
    applications = job.applications.all().select_related('applicant')
    
    status_filter = request.GET.get('status')
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    applications = paginator.get_page(page_number)
    
    context = {
        'job': job,
        'applications': applications,
        'status_choices': Application.STATUS_CHOICES,
    }
    return render(request, "jobs/job_applications.html", context)


@login_required
def update_application_status(request, pk):
    application = get_object_or_404(Application, pk=pk, job__posted_by=request.user)
    
    if request.method == "POST":
        status = request.POST.get('status')
        if status in dict(Application.STATUS_CHOICES):
            application.status = status
            application.save()
            messages.success(request, f"Application status updated to {application.get_status_display()}")
    
    return redirect("jobs:job_applications", pk=application.job.pk)
