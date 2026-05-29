from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from .forms import ContactMessageForm
from .models import Blog, Profile, Project


class HomeView(FormView):
    template_name = "portfolio/home.html"
    form_class = ContactMessageForm
    success_url = reverse_lazy("portfolio:home")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Thanks for reaching out. I'll reply soon.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        context["profile"] = profile
        if profile and profile.skills:
            context["skills_list"] = [
                skill.strip() for skill in profile.skills.split(",") if skill.strip()
            ]
        else:
            context["skills_list"] = []
        context["projects"] = Project.objects.order_by("-created_at")[:6]
        context["blogs"] = Blog.objects.filter(is_published=True).order_by("-created_at")[:3]
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = "portfolio/blog_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context
