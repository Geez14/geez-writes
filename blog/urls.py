from django.urls import path

# from . import views
from .views import HomeView, DetailedPostView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", DetailedPostView.as_view(), name="article-detail"),
]