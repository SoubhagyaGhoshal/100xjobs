from django import forms
from .models import Job, Application, Company, Category


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title", "description", "requirements", "responsibilities",
            "salary_min", "salary_max", "salary_currency", "location",
            "employment_type", "work_mode", "experience_level",
            "skills_required", "company", "category", "application_deadline"
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Job Description'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Job Requirements'}),
            'responsibilities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Key Responsibilities'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Salary'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Maximum Salary'}),
            'salary_currency': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Location'}),
            'employment_type': forms.Select(attrs={'class': 'form-select'}),
            'work_mode': forms.Select(attrs={'class': 'form-select'}),
            'experience_level': forms.Select(attrs={'class': 'form-select'}),
            'skills_required': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Required skills (comma-separated)'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'application_deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["cover_letter"]  # Removed resume field temporarily
        widgets = {
            'cover_letter': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Write your cover letter here...'
            }),
        }


class JobSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search jobs by title, company, or keywords...'
        })
    )
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Location'
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    employment_type = forms.ChoiceField(
        choices=[('', 'All Types')] + Job.EMPLOYMENT_TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    work_mode = forms.ChoiceField(
        choices=[('', 'All Modes')] + Job.WORK_MODE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    experience_level = forms.ChoiceField(
        choices=[('', 'All Levels')] + Job.EXPERIENCE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    salary_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Min Salary'
        })
    )
