from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import JobPosting, Profile

@require_http_methods(["GET"])
def get_profiles(request):
    designation = request.GET.get('designation')
    location = request.GET.get('location')
    company = request.GET.get('company')
    
    profiles = Profile.objects.filter(
        title__icontains=designation,
        location__icontains=location,
        current_company__icontains=company
    )[:10]
    
    return JsonResponse({
        'profiles': [
            {
                'name': p.name,
                'title': p.title,
                'location': p.location,
                'current_company': p.current_company,
                'skills': p.skills,
                'match_score': calculate_match_score(p, designation, location, company)
            }
            for p in profiles
        ]
    })

@require_http_methods(["GET"])
def get_jobs(request):
    title = request.GET.get('title')
    location = request.GET.get('location')
    experience = request.GET.get('experience')
    
    jobs = JobPosting.objects.filter(
        title__icontains=title,
        location__icontains=location
    )[:10]
    
    return JsonResponse({
        'jobs': [
            {
                'title': j.title,
                'company': j.company,
                'location': j.location,
                'description': j.description,
                'skills_required': j.skills_required,
                'match_score': calculate_job_match_score(j, title, location, experience)
            }
            for j in jobs
        ]
    })

def calculate_match_score(profile, designation, location, company):
    score = 0
    if designation.lower() in profile.title.lower():
        score += 0.4
    if location.lower() in profile.location.lower():
        score += 0.3
    if company.lower() in profile.current_company.lower():
        score += 0.3
    return round(score, 2)

def calculate_job_match_score(job, title, location, experience):
    score = 0
    if title.lower() in job.title.lower():
        score += 0.5
    if location.lower() in job.location.lower():
        score += 0.5
    return round(score, 2)