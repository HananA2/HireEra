from django.urls import path
from . import views

app_name = "seeker"

urlpatterns = [

    path("login/", views.login_view, name="signin"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.sign_out, name="logout"),

    path("save/<int:job_id>/", views.save_job, name="save_job"),
    path("saved/", views.saved_jobs, name="saved_jobs"),
    path("profile/", views.profile, name="profile"),
]

    # path("login/", views.sign_in, name="signin"),
    # path("signup/", views.sign_up, name="signup"),
    # path("logout/", views.sign_out, name="logout"),
    # path("save/<int:job_id>/", views.save_job, name="save_job"),
    # path("saved/", views.saved_jobs, name="saved_jobs"),
    # path("profile/", views.profile, name="profile"),