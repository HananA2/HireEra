from django.db import models
from django.conf import settings   
from jobs.models import Job


class Application(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,     
        on_delete=models.CASCADE,
        related_name="applications"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to="resumes/")

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} → {self.job.title}"
