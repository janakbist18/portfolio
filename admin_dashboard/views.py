from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from portfolio.models import Blog, ContactMessage, Profile, Project

from .forms import BlogForm, DashboardLoginForm, ProfileForm, ProjectForm


class DashboardLoginView(LoginView):
    template_name = "admin_dashboard/login.html"
    authentication_form = DashboardLoginForm


class DashboardLogoutView(LogoutView):
    pass


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "admin_dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_count"] = Project.objects.count()
        context["blog_count"] = Blog.objects.count()
        context["message_count"] = ContactMessage.objects.count()
        context["latest_messages"] = ContactMessage.objects.order_by("-created_at")[:5]

        since = timezone.now() - timedelta(days=180)
        monthly = (
            ContactMessage.objects.filter(created_at__gte=since)
            .annotate(month=TruncMonth("created_at"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )
        context["chart_labels"] = [row["month"].strftime("%b %Y") for row in monthly]
        context["chart_data"] = [row["total"] for row in monthly]
        return context


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "admin_dashboard/projects/list.html"
    context_object_name = "projects"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "admin_dashboard/projects/form.html"
    success_url = reverse_lazy("admin_dashboard:projects")


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "admin_dashboard/projects/form.html"
    success_url = reverse_lazy("admin_dashboard:projects")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "admin_dashboard/projects/confirm_delete.html"
    success_url = reverse_lazy("admin_dashboard:projects")


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "admin_dashboard/blog/list.html"
    context_object_name = "posts"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "admin_dashboard/blog/form.html"
    success_url = reverse_lazy("admin_dashboard:blog")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "admin_dashboard/blog/form.html"
    success_url = reverse_lazy("admin_dashboard:blog")


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "admin_dashboard/blog/confirm_delete.html"
    success_url = reverse_lazy("admin_dashboard:blog")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "admin_dashboard/profile/form.html"
    success_url = reverse_lazy("admin_dashboard:profile")

    def get_object(self, queryset=None):
        profile = Profile.objects.first()
        if profile is None:
            profile = Profile.objects.create(name="Your Name", role="Your Role", bio="")
        return profile


class MessageListView(LoginRequiredMixin, ListView):
    model = ContactMessage
    template_name = "admin_dashboard/messages/list.html"
    context_object_name = "messages"
