from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# -----------------------------
# Login Form
# -----------------------------
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()

        username = cleaned.get("username")
        password = cleaned.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password.")
            self.user = user  

        return cleaned


# -----------------------------
# Signup Form
# -----------------------------
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already used.")
        return email

    # -----------------------------
    # PASSWORD VALIDATION
    # -----------------------------
    def clean_password(self):
        password = self.cleaned_data.get("password")

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if not any(c.isupper() for c in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")

        if not any(c.islower() for c in password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")

        if not any(c.isdigit() for c in password):
            raise forms.ValidationError("Password must contain at least one number.")

        if not any(c in "!@#$%^&*()_+" for c in password):
            raise forms.ValidationError("Password must contain at least one symbol (!@#$%^&*).")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


# -----------------------------
# Profile Update Form
# -----------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
