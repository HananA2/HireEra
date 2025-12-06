from django import forms
from .models import Application
import re

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["full_name", "email", "phone", "resume"]

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not re.match(r"^05\d{8}$", phone):
            raise forms.ValidationError("Phone number must start with 05 and contain 10 digits.")
        return phone

    def clean_resume(self):
        resume = self.cleaned_data.get("resume")
        if not resume:
            raise forms.ValidationError("Please upload your resume.")
        return resume

    def clean_full_name(self):
        name = self.cleaned_data.get("full_name")
        if not name:
            raise forms.ValidationError("Name is required.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email is required.")
        return email
