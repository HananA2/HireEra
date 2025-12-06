from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import Job

User = get_user_model()  # استخدام الـ Custom User Model


# ====== تسجيل دخول الـ Employer ======

class EmployerLoginView(LoginView):
    """
    صفحة تسجيل الدخول الخاصة بالـ employer.
    بعد تسجيل الدخول يروح مباشرة لصفحة الداشبورد.
    """
    template_name = "employer/employer_login.html"

    def get_success_url(self):
        # اسم الـ URL داخل employer/urls.py لازم يكون name="dashboard"
        return reverse_lazy("employer:dashboard")


# ====== تسجيل حساب جديد للـ Employer ======

def employer_signup(request):
    """
    صفحة إنشاء حساب جديد لصاحب عمل (Employer).
    نستخدم الـ User المخصص للمشروع عن طريق get_user_model().
    """
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # التحقق من تعبئة الحقول
        if not username or not email or not password:
            messages.error(request, "Please fill in all fields.")
            return redirect("employer:signup")

        # التحقق من تكرار اسم المستخدم أو الإيميل
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect("employer:signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect("employer:signup")

        # إنشاء المستخدم
        User.objects.create_user(username=username, email=email, password=password)

        messages.success(request, "Account created successfully. Please sign in.")
        return redirect("employer:login")

    return render(request, "employer/employer_signup.html")


# ====== صفحات الداشبورد والوظائف ======

def employer_dashboard(request):
    return render(request, "employer/employer_dashboard.html")


def employer_jobs(request):
    """
    صفحة عرض الوظائف الخاصة بالـ employer.
    حالياً نعرض كل الوظائف، وبعدين تقدرون تقيدونها بمالك الوظيفة.
    """
    jobs = Job.objects.all().order_by("-created_at")
    return render(request, "employer/jobs.html", {"jobs": jobs})


def post_job(request):
    """
    صفحة نشر وظيفة جديدة.
    """
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
    """
    حذف وظيفة من قائمة الوظائف.
    """
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect("employer:jobs")


def employer_profile(request):
    """
    صفحة بروفايل صاحب العمل (تقدرون تطورونها لاحقاً).
    """
    return render(request, "employer/employer_profile.html")


def applicants_list(request):
    """
    صفحة قائمة المتقدّمين (Candidates / Applicants).
    حالياً نرسل قائمة فاضية عشان التمبلت يشتغل بدون أخطاء،
    تقدرون لاحقاً تربطونها بموديل JobApplication.
    """
    applicants = []
    return render(request, "employer/applicants_list.html", {"applicants": applicants})


def employer_candidates(request):
    return HttpResponse("Candidates page (to be designed)")


def employer_interviews(request):
    return HttpResponse("Interviews page (to be designed)")


def employer_analytics(request):
    return HttpResponse("Analytics page (to be designed)")


def employer_tools(request):
    return HttpResponse("Tools page (to be designed)")
