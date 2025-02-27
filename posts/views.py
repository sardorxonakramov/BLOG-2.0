from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
    model=Post
    template_name='posts/index.html'
    context_object_name='posts'
    ordering=['-created_at']
    
class PostDetailView(DetailView):
    model=Post
    template_name='posts/detail.html'
    context_object_name='post'