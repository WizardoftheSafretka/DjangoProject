from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product

class HomeListView(ListView):
    model = Product

class HomeDetailView(DetailView):
    model = Product

class HomeCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

class HomeUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get('pk')])

class HomeDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
