from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import Blog


class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "image", "is_published")
    success_url = reverse_lazy("blogs:blogs_list")

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "image", "is_published")
    success_url = reverse_lazy("blogs:blogs_list")

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blogs_list")
