from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_products_by_category


class OwnerRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, 'Только владелец может редактировать этот продукт.')
        return redirect('product_detail', pk=self.kwargs.get('pk'))


class OwnerOrModeratorRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        product = self.get_object()
        is_owner = product.owner == self.request.user
        is_moderator = self.request.user.has_perm('catalog.delete_product')
        return is_owner or is_moderator

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для удаления этого продукта.')
        return redirect('product_detail', pk=self.kwargs.get('pk'))

class HomeListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = cache.get('products_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('products_queryset', queryset, 60 * 15)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

@method_decorator(cache_page(60 * 15), name='dispatch')
class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Product

class HomeCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class HomeUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get('pk')])


class HomeDeleteView(LoginRequiredMixin, OwnerOrModeratorRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_pk):
        product = get_object_or_404(Product, id=product_pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации.")

        product.is_published = True
        product.save()

        return redirect('catalog:product_detail', product_id=product.pk)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = get_products_by_category(self.object.id)
        context['categories'] = Category.objects.all()
        return context