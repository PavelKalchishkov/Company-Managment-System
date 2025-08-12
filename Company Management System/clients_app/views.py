from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import ClientCreateForm, ClientUpdateForm
from .models import Client


class ClientsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Client
    template_name = 'table_views/clients/clients.html'
    context_object_name = 'clients'
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            terms = query.strip().split()

            if len(terms) == 1:
                queryset = queryset.filter(
                    Q(first_name__icontains=terms[0]) |
                    Q(last_name__icontains=terms[0]) |
                    Q(phone_number__icontains=terms[0])
                )

            elif len(terms) >= 2:
                queryset = queryset.filter(
                    (Q(first_name__icontains=terms[0]) & Q(last_name__icontains=terms[1])) |
                    (Q(first_name__icontains=terms[1]) & Q(last_name__icontains=terms[0])) |
                    Q(phone_number__icontains=query)
                )

        return queryset

    permission_required = 'clients_app.view_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context


class ClientsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientCreateForm
    template_name = 'table_views/clients/clients_add.html'
    success_url = reverse_lazy('clients_view')

    permission_required = 'clients_app.add_client'

class ClientsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/clients/clients_update.html'
    success_url = reverse_lazy('clients_view')

    permission_required = 'clients_app.change_client'


class ClientsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    pk_url_kwarg = 'pk'
    template_name = 'table_views/clients/clients_delete.html'
    success_url = reverse_lazy('clients_view')

    permission_required = 'clients_app.delete_client'


class ClientsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Client
    pk_url_kwarg = 'pk'
    template_name = 'table_views/clients/clients_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['client'] = self.get_object()

        return context

    permission_required = 'clients_app.view_client'

