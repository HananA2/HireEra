from django.urls import path
from . import views
from .views import EmployerLoginView

app_name = "employer"

urlpatterns = [

    # ===== Authentication =====
    path("login/", EmployerLoginView.as_view(), name="login"),

    # ===== Main Dashboard =====
    path("dashboard/", views.employer_dashboard, name="dashboard"),

    # ===== Jobs =====
    path("jobs/", views.employer_jobs, name="jobs"),
    path("post-job/", views.post_job, name="post_job"),
    path("delete-job/<int:job_id>/", views.delete_job, name="delete_job"),

    # ===== Applicants / Candidates =====
    path("applicants/", views.applicants_list, name="applicants"),
    path("candidates/", views.employer_candidates, name="candidates"),

    # ===== Other Pages =====
    path("interviews/", views.employer_interviews, name="interviews"),
    path("analytics/", views.employer_analytics, name="analytics"),
    path("tools/", views.employer_tools, name="tools"),
    path("profile/", views.employer_profile, name="profile"),
    path("signup/", views.employer_signup, name="signup"),
]
