from django.urls import path

from .views import BlogDetailView, HomeView

app_name = "portfolio"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
