from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='seeker'
    )

    def is_seeker(self):
        return self.role == 'seeker'

    def is_employer(self):
        return self.role == 'employer'

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name
