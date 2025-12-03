from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def employer_dashboard(request):
    """
    صفحة لوحة تحكم صاحب العمل (Employer Dashboard)
    """
    context = {
        "page_title": "Employer Dashboard",
    }
    return render(request, "employer/employer_dashboard.html", context)
