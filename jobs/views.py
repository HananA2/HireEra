from django.shortcuts import render
from .models import Job
from django.utils import timezone
from datetime import timedelta
from seeker.models import SavedJob

def search_view(request):

    q = request.GET.get("q", "")
    job_type = request.GET.get("job_type", "")
    location = request.GET.get("location", "")
    date_posted = request.GET.get("date_posted", "")
    loc = request.GET.get("loc", "")

    jobs = Job.objects.all()

    # keyword
    if q:
        jobs = jobs.filter(title__icontains=q)

    # loc filter
    if loc:
        jobs = jobs.filter(location__icontains=loc)

    # job type filter
    if job_type:
        jobs = jobs.filter(job_type=job_type)

    # location filter
    if location:
        jobs = jobs.filter(location__icontains=location)

    # date posted
    if date_posted:
        days = int(date_posted)
        cutoff = timezone.now() - timedelta(days=days)
        jobs = jobs.filter(date_posted__gte=cutoff)

    # return render(request, "jobs/search.html", {"jobs": jobs})
    saved_jobs = []
    if request.user.is_authenticated:
        saved_jobs = list(
            SavedJob.objects.filter(user=request.user)
            .values_list("job_id", flat=True)
        )
    return render(request, "jobs/search.html", {
        "jobs": jobs,
        "saved_jobs": saved_jobs
    })
