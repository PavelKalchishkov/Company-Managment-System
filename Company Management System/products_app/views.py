from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import ProductCreateForm, ProductUpdateForm
from .models import Product

class ProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'table_views/products/products.html'
    context_object_name = 'products'

    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'table_views/products/products_add.html'
    success_url = reverse_lazy('products_view')

    def form_valid(self, form):
        product = form.save()
        product.name += str(f'-{product.vendor}')
        product.save()

        return redirect('products_view')

class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/products/products_update.html'
    success_url = reverse_lazy('products_view')

class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    pk_url_kwarg = 'pk'
    template_name = 'table_views/products/products_delete.html'
    success_url = reverse_lazy('products_view')

class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Product
    pk_url_kwarg = 'pk'
    template_name = 'table_views/products/products_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['product'] = self.get_object()

        return context