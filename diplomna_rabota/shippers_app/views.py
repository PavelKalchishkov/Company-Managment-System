from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ShipperCreationForm, ShipperUpdateForm
from .models import Shipper


class ShippersView(LoginRequiredMixin, ListView):
    model = Shipper
    template_name = 'table_views/shippers/shippers.html'
    context_object_name = 'shippers'

    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class ShippersAddView(LoginRequiredMixin, CreateView):
    model = Shipper
    form_class = ShipperCreationForm
    template_name = 'table_views/shippers/shippers_add.html'
    success_url = reverse_lazy('shippers_view')

class ShippersUpdateView(LoginRequiredMixin, UpdateView):
    model = Shipper
    form_class = ShipperUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/shippers/shippers_update.html'
    success_url = reverse_lazy('shippers_view')

class ShippersDeleteView(LoginRequiredMixin, DeleteView):
    model = Shipper
    pk_url_kwarg = 'pk'
    template_name = 'table_views/shippers/shippers_delete.html'
    success_url = reverse_lazy('shippers_view')


