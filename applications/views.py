from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicationForm
from jobs.models import Job
from django.contrib.auth.decorators import login_required

@login_required
def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()

            return redirect("applications:success")
        else:
            # Shows errors in page (same styling as signup)
            print(form.errors)

    else:
        form = ApplicationForm(initial={
            "full_name": f"{request.user.first_name} {request.user.last_name}",
            "email": request.user.email
        })


    return render(request, "applications/apply.html", {
        "form": form,
        "job": job,
    })

def success(request):
    return render(request, "applications/success.html")
