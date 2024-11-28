from django.urls import path

# from . import views
from .views import HomeView, DetailedPostView, AddPostView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/<int:pk>", DetailedPostView.as_view(), name="blog-detail"),
    path("add-post/", AddPostView.as_view(), name="add-post"),
]