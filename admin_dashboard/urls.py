from django.urls import path

from .views import (
    BlogCreateView,
    BlogDeleteView,
    BlogListView,
    BlogUpdateView,
    DashboardLoginView,
    DashboardLogoutView,
    DashboardView,
    MessageListView,
    ProfileUpdateView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectListView,
    ProjectUpdateView,
)

app_name = "admin_dashboard"

urlpatterns = [
    path("login/", DashboardLoginView.as_view(), name="login"),
    path("logout/", DashboardLogoutView.as_view(), name="logout"),
    path("", DashboardView.as_view(), name="dashboard"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("projects/new/", ProjectCreateView.as_view(), name="project_create"),
    path("projects/<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_edit"),
    path("projects/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
    path("blog/", BlogListView.as_view(), name="blog"),
    path("blog/new/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("blog/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("messages/", MessageListView.as_view(), name="messages"),
]
