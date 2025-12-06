from django.urls import path
from . import views

app_name = "employer"

urlpatterns = [
    path("dashboard/", views.employer_dashboard, name="dashboard"),

    path("jobs/", views.employer_jobs, name="jobs"),
    path("candidates/", views.employer_candidates, name="candidates"),
    path("interviews/", views.employer_interviews, name="interviews"),
    path("analytics/", views.employer_analytics, name="analytics"),
    path("tools/", views.employer_tools, name="tools"),

    path("post-job/", views.post_job, name="post_job"),
    path("delete-job/<int:job_id>/", views.delete_job, name="delete_job"),
    path("profile/", views.employer_profile, name="profile"),
    path("applicants/", views.applicants_list, name="applicants"),
]
