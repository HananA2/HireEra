# from django.shortcuts import render, redirect

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError
# from django.urls import reverse

# from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from jobs.models import Job
# from .models import SavedJob
# from applications.models import Application

# def signup_view(request):

#     errors = {}

#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         password = request.POST.get("password")

        
#         try:
#             validate_email(email)
#         except ValidationError:
#             errors["email"] = "Please enter a valid email address"

#         if User.objects.filter(email=email).exists():
#             errors["email"] = "Email is already in use"

#         if User.objects.filter(username=username).exists():
#             errors["username"] = "Username is already taken"

#         password_errors = []

#         if len(password) < 8:
#             password_errors.append("Must be at least 8 characters")

#         if not any(c.isupper() for c in password):
#             password_errors.append("Must include at least one uppercase letter")

#         specials = "!@#$%^&*()-_=+[]{};:,.<>?/|"
#         if not any(c in specials for c in password):
#             password_errors.append("Must include at least one special character")

#         if password_errors:
#             errors["password"] = password_errors

#         if not errors:
#             new_user = User.objects.create_user(
#                 username=username,
#                 password=password,
#                 email=email,
#                 first_name=first_name,
#                 last_name=last_name,
#             )
#             return redirect("seeker:signin")

#         return render(request, "seeker/signup.html", {"errors": errors})

#     return render(request, "seeker/signup.html")

# def signin_view(request):
#     error = False

#     if request.method == "POST":
#         user = authenticate(
#             request,
#             username=request.POST["username"],
#             password=request.POST["password"]
#         )

#         if user:
#             login(request, user)
#             return redirect(request.GET.get("next", reverse("jobs:search")))
#         else:
#             error = True  

#     return render(request, "seeker/signin.html", {"error": error})


# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged out successfully")
#     return redirect("/")

# from django.http import JsonResponse

# @login_required
# def save_job(request, job_id):
#     job = get_object_or_404(Job, id=job_id)
#     saved, created = SavedJob.objects.get_or_create(user=request.user, job=job)

#     if not created:
#         saved.delete()
#         return JsonResponse({"status": "removed"})

#     return JsonResponse({"status": "saved"})

# @login_required
# def saved_jobs(request):
#     saved = SavedJob.objects.filter(user=request.user)
#     applied = Application.objects.filter(user=request.user)

#     tab = request.GET.get("tab", "saved")  # default tab

#     return render(request, "seeker/saved_jobs.html", {
#         "saved": saved,
#         "applied": applied,
#         "active_tab": tab,
#     })

# @login_required
# def profile(request):
#     return render(request, "seeker/profile.html")

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm, SignupForm, ProfileForm

from django.http import JsonResponse
from jobs.models import Job
from .models import SavedJob
from django.shortcuts import get_object_or_404


# -----------------------------
# SIGN IN
# -----------------------------
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            login(request, form.user)
            return redirect("jobs:search")

        # messages.error(request, "Invalid username or password.")

    return render(request, "seeker/signin.html", {"form": form})

# -----------------------------
# SIGN UP
# -----------------------------
def signup_view(request):
    form = SignupForm(request.POST or None)

    errors = {}  # نجمع الأخطاء هنا

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("seeker:signin")

        # جمع الأخطاء من الفورم
        for field, msgs in form.errors.items():
            errors[field] = msgs[0]

    return render(request, "seeker/signup.html", {
        "form": form,
        "errors": errors,
    })
# -----------------------------
# LOGOUT
# -----------------------------
def sign_out(request):
    logout(request)
    return redirect("home_view")   # أو أي صفحة تبينها


# -----------------------------
# PROFILE PAGE 
# -----------------------------
@login_required
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")

    return render(request, "seeker/profile.html", {"form": form})

# -----------------------------
# SAVE JOB 
# -----------------------------

@login_required
def save_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    saved, created = SavedJob.objects.get_or_create(user=request.user, job=job)

    if not created:
        saved.delete()
        return JsonResponse({"status": "removed"})

    return JsonResponse({"status": "saved"})

@login_required
def saved_jobs(request):

    tab = request.GET.get("tab", "saved")

    # Saved jobs
    saved = SavedJob.objects.filter(user=request.user)

    # Applied jobs
    from applications.models import Application
    applied = Application.objects.filter(user=request.user)

    context = {
        "saved": saved,
        "applied": applied,
        "active_tab": tab,
    }

    return render(request, "seeker/saved_jobs.html", context)
