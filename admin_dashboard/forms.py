from django import forms
from django.contrib.auth.forms import AuthenticationForm

from portfolio.models import Blog, Profile, Project


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"form-control {css_class}".strip()


class ProfileForm(BaseModelForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "role",
            "bio",
            "image",
            "cv",
            "skills",
            "social_github",
            "social_linkedin",
            "social_twitter",
            "social_email",
            "social_website",
        ]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 5}),
            "skills": forms.Textarea(attrs={"rows": 3, "placeholder": "Python, Django, React"}),
        }


class ProjectForm(BaseModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "image",
            "tech_stack",
            "link",
            "featured",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "tech_stack": forms.TextInput(attrs={"placeholder": "Django, Tailwind, SQLite"}),
        }


class BlogForm(BaseModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "image", "is_published"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 6}),
        }


class DashboardLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )
