from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job


def employer_dashboard(request):
    return render(request, "employer/employer_dashboard.html")


def post_job(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location_type = request.POST.get("location_type")
        location = request.POST.get("location")
        salary_from = request.POST.get("salary_from") or None
        salary_to = request.POST.get("salary_to") or None
        currency = request.POST.get("currency") or "SAR"
        description = request.POST.get("description") or ""

        if title and location_type and location:
            Job.objects.create(
                employer=request.user if request.user.is_authenticated else None,
                title=title,
                location_type=location_type,
                location=location,
                salary_from=salary_from,
                salary_to=salary_to,
                currency=currency,
                description=description,
                status="active",
            )
            return redirect("employer:jobs")

    return render(request, "employer/post_job.html")

def delete_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect("employer:jobs")

def employer_profile(request):
    return render(request, "employer/employer_profile.html")


def applicants_list(request):
    return render(request, "employer/applicants_list.html")


def employer_jobs(request):
    jobs = Job.objects.all().order_by("-created_at")
    return render(request, "employer/jobs.html", {"jobs": jobs})


def employer_candidates(request):
    return HttpResponse("Candidates page (to be designed)")


def employer_interviews(request):
    return HttpResponse("Interviews page (to be designed)")


def employer_analytics(request):
    return HttpResponse("Analytics page (to be designed)")


def employer_tools(request):
    return HttpResponse("Tools page (to be designed)")
