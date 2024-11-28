from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class HomeView(ListView):
    model = BlogPost
    template_name = 'index.html'
    
class DetailedPostView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'