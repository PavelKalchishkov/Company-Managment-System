from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import VendorCreationForm, VendorUpdateForm
from .models import Vendor


class VendorsView(LoginRequiredMixin, ListView):
    model = Vendor
    template_name = 'table_views/vendors/vendors.html'
    context_object_name = 'vendors'

    ordering = ['id']

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

class VendorsAddView(LoginRequiredMixin, CreateView):
    model = Vendor
    form_class = VendorCreationForm
    template_name  = 'table_views/vendors/vendors_add.html'
    success_url = reverse_lazy('vendors_view')


class VendorsUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendor
    form_class = VendorUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/vendors/vendors_update.html'
    success_url = reverse_lazy('vendors_view')

class VendorsDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendor
    pk_url_kwarg = 'pk'
    template_name = 'table_views/vendors/vendors_delete.html'
    success_url = reverse_lazy('vendors_view')





