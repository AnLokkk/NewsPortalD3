from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'NEWS.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'new1.html'
    context_object_name = 'new1'

