from django.db import models
from django.conf import settings     
from jobs.models import Job


class SavedJob(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,      
        on_delete=models.CASCADE,
        related_name="saved_jobs"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user} saved {self.job.title}"


class AppliedJob(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,      
        on_delete=models.CASCADE,
        related_name="applied_jobs"
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} applied to {self.job.title}"
