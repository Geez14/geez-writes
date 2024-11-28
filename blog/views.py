from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *

class HomeView(ListView):
    model = BlogPost
    template_name = 'index.html'
    
class DetailedPostView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = BlogPost
    template_name = 'add_post.html'
    fields = '__all__'
    # we can use cherry pick too as many of the items can be null
    # fields = ('title', 'body')