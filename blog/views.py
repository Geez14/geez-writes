from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import PostForm

from .forms import PostForm


class HomeView(ListView):
    model = BlogPost
    template_name = 'index.html'
    
class DetailedPostView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' # we have to remove this because of form_class!
    # we can use cherry pick too as many of the items can be null
    # fields = ('title', 'body')

class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' # we have to remove this because of form_class!
    # we can use cherry pick too as many of the items can be null
    # fields = ('title', 'body')