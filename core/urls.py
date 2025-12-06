from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home_view, name="home_view"),

    # Logout URL
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("core:home_view")),
        name="logout"
    ),
]
