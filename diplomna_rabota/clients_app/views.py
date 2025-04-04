from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ClientCreateForm, ClientUpdateForm
from .models import Client


class ClientsView(ListView, LoginRequiredMixin):
    model = Client
    template_name = 'table_views/clients/clients.html'
    context_object_name = 'clients'

    ordering = ['first_name', 'last_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class ClientsCreateView(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientCreateForm
    template_name = 'table_views/clients/clients_add.html'
    success_url = reverse_lazy('clients_view')

class ClientsUpdateView(UpdateView, LoginRequiredMixin):
    model = Client
    form_class = ClientUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/clients/clients_update.html'
    success_url = reverse_lazy('clients_view')

class ClientsDeleteView(DeleteView, LoginRequiredMixin):
    model = Client
    pk_url_kwarg = 'pk'
    template_name = 'table_views/clients/clients_delete.html'
    success_url = reverse_lazy('clients_view')
