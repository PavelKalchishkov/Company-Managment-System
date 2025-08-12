from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import ShipperCreationForm, ShipperUpdateForm
from .models import Shipper


class ShippersView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Shipper
    template_name = 'table_views/shippers/shippers.html'
    context_object_name = 'shippers'
    ordering = ['-id']

    permission_required = 'shippers_app.view_shipper'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class ShippersAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Shipper
    form_class = ShipperCreationForm
    template_name = 'table_views/shippers/shippers_add.html'
    success_url = reverse_lazy('shippers_view')

    permission_required = 'shippers_app.add_shipper'

class ShippersUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Shipper
    form_class = ShipperUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/shippers/shippers_update.html'
    success_url = reverse_lazy('shippers_view')

    permission_required = 'shippers_app.change_shipper'

class ShippersDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Shipper
    pk_url_kwarg = 'pk'
    template_name = 'table_views/shippers/shippers_delete.html'
    success_url = reverse_lazy('shippers_view')

    permission_required = 'shippers_app.delete_shipper'

class ShippersDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Shipper
    pk_url_kwarg = 'pk'
    template_name = 'table_views/shippers/shippers_details.html'

    permission_required = 'shippers_app.view_shipper'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['shipper'] = self.get_object()

        return context