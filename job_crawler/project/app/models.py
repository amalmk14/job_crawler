from django.db import models

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    current_company = models.CharField(max_length=200)
    skills = models.TextField()
    url = models.URLField(unique=True)
    crawled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.title}"
