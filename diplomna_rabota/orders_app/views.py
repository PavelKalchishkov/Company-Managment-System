from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import OrderProduct

from .forms import OrderCreationForm, OrderUpdateForm
from .models import Order


class OrdersView(ListView, LoginRequiredMixin):
    model = Order
    template_name = 'table_views/orders/orders.html'
    context_object_name = 'orders'

    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['order_products'] = OrderProduct.objects.all()
        return context


class OrdersCreateView(CreateView, LoginRequiredMixin):
    model = Order
    form_class = OrderCreationForm
    template_name = 'table_views/orders/orders_add.html'
    success_url = reverse_lazy('orders_view')

class OrdersUpdateView(UpdateView, LoginRequiredMixin):
    model = Order
    form_class = OrderUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/orders/orders_update.html'
    success_url = reverse_lazy('orders_view')

class OrdersDeleteView(DeleteView, LoginRequiredMixin):
    model = Order
    pk_url_kwarg = 'pk'
    template_name = 'table_views/orders/orders_delete.html'
    success_url = reverse_lazy('orders_view')