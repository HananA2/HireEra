from django.urls import path
from . import views

app_name = "employer"

urlpatterns = [
    path("dashboard/", views.employer_dashboard, name="dashboard"),
]
