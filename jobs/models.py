from django.db import models
from django.utils import timezone

JOB_TYPES = [
    ("full-time", "Full-time"),
    ("part-time", "Part-time"),
    ("remote", "Remote"),
    ("contract", "Contract"),
    ("internship", "Internship"),
]

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)  # لاحقاً نربطها بعلاقة Employer
    location = models.CharField(max_length=255)

    job_type = models.CharField(max_length=20, choices=JOB_TYPES)
    description = models.TextField()

    date_posted = models.DateTimeField(default=timezone.now)

    salary = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.company}"
