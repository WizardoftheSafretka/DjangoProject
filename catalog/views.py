from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product

class HomeListView(ListView):
    model = Product

class HomeDetailView(DetailView):
    model = Product


