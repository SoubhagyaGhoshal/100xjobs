# 100xJobs - Professional Job Portal

A comprehensive job portal web application built with Django, featuring modern UI, role-based authentication, and advanced job management capabilities. This project demonstrates a complete full-stack web application similar to professional job boards like the staging site at https://staging.placements.100xdevs.com/.

## 🌟 Features

### For Job Seekers
- **User Registration & Authentication** with role selection (Job Seeker/Employer)
- **Advanced Job Search** with filters (location, category, employment type, work mode, salary)
- **Job Applications** with cover letter and resume upload
- **Saved Jobs** functionality to bookmark interesting positions
- **Application Tracking** to monitor application status
- **Responsive Design** that works on all devices

### For Employers
- **Employer Dashboard** with comprehensive analytics
- **Job Posting** with detailed job descriptions, requirements, and compensation
- **Application Management** with status tracking (pending, reviewed, shortlisted, rejected, hired)
- **Job Management** (create, edit, delete, activate/deactivate)
- **Candidate Review** with resume viewing and application filtering

### For Administrators
- **Django Admin Integration** with enhanced interfaces
- **User Management** with role-based permissions
- **Content Management** for companies, categories, testimonials, and FAQs
- **System Analytics** and reporting

## 🛠 Tech Stack

- **Backend**: Django 5.2.7 (Python web framework)
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3, Bootstrap Icons
- **Authentication**: Django's built-in authentication system
- **File Handling**: Django's file upload system with Pillow
- **Deployment**: Gunicorn + WhiteNoise for static files

## 📁 Project Structure

```
jobportal/
├── jobportal/              # Django project settings
│   ├── settings.py         # Main settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── jobs/                   # Jobs application
│   ├── models.py          # Job, Application, SavedJob, etc.
│   ├── views.py           # Business logic
│   ├── forms.py           # Form definitions
│   ├── admin.py           # Admin interface
│   └── management/        # Custom management commands
├── accounts/               # User authentication
│   ├── models.py          # UserProfile model
│   ├── forms.py           # Registration forms
│   └── views.py           # Auth views
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── jobs/              # Job-related templates
│   └── accounts/          # Authentication templates
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User uploads (resumes, images)
├── requirements.txt        # Python dependencies
├── setup.py               # Automated setup script
└── README.md              # This file
```

## 🚀 Quick Setup

### Option 1: Automated Setup (Recommended)
```bash
# Clone or download the project
cd jobportal

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run automated setup
python setup.py
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate sample data (optional)
python manage.py populate_sample_data

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

## 🌐 Access Points

- **Main Application**: https://one00xjobs.onrender.com/
- **Admin Panel**: https://one00xjobs.onrender.com/admin/login/?next=/admin/

## 👥 Test Accounts

After running the setup script, you can use these test accounts:

### Administrator
- **Username**: admin
- **Password**: ********
- **Access**: Full system administration

### Employers (employer1-5)
- **Username**: employer1, employer2, etc.
- **Password**: password123
- **Features**: Post jobs, manage applications

### Job Seekers (jobseeker1-10)
- **Username**: jobseeker1, jobseeker2, etc.
- **Password**: password123
- **Features**: Browse jobs, apply, save jobs

## 📊 Database Models

### Core Models
- **User**: Extended with UserProfile for role-based access
- **Company**: Job posting organizations
- **Category**: Job categories with SEO-friendly slugs
- **Job**: Comprehensive job postings with all modern fields
- **Application**: Job applications with status tracking
- **SavedJob**: User's bookmarked jobs

### Additional Models
- **Testimonial**: User success stories
- **FAQ**: Frequently asked questions
- **UserProfile**: Extended user information with roles

## 🎨 UI/UX Features

- **Modern Design**: Clean, professional interface inspired by leading job boards
- **Responsive Layout**: Mobile-first design that works on all screen sizes
- **Interactive Elements**: Hover effects, smooth transitions, and intuitive navigation
- **Bootstrap Integration**: Consistent styling with Bootstrap 5 components
- **Icon System**: Bootstrap Icons for visual clarity
- **Color Coding**: Status badges and visual indicators for better UX

## 🔧 Advanced Features

### Search & Filtering
- Full-text search across job titles, descriptions, and company names
- Advanced filters: location, category, employment type, work mode, experience level, salary range
- Pagination for large result sets

### Application Management
- Status tracking: pending → reviewed → shortlisted → rejected/hired
- Resume upload and viewing
- Cover letter support
- Application history for both job seekers and employers

### Dashboard Analytics
- Employer dashboard with job posting statistics
- Application metrics and recent activity
- Job performance tracking

## 🚀 Deployment

The application is production-ready with:

- **Gunicorn** for WSGI server
- **WhiteNoise** for static file serving
- **PostgreSQL** support for production databases
- **Environment variables** for sensitive settings
- **Security settings** configured for production

### Environment Variables
Create a `.env` file for production:
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:pass@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 📝 API Integration (Future Enhancement)

The codebase is structured to easily integrate external job APIs:
- Management commands for data import
- Flexible model structure
- API-ready serialization patterns

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 📈 Performance Optimizations

- Database query optimization with `select_related` and `prefetch_related`
- Pagination for large datasets
- Efficient filtering and search
- Static file optimization with WhiteNoise

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License. 

## 📞 Support

For questions or issues, please refer to the documentation or create an issue in the project repository.

---

**Built with ❤️ for the 100xDevs community**
