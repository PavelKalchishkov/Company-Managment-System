from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import CompanyCreateForm, CompanyUpdateForm, InvoiceCreateForm, InvoiceUpdateForm, InvoiceReportFilter
from .models import Company, Invoice
from orders_app.models import OrderProduct


class CompaniesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Company
    template_name = 'table_views/companies/companies.html'
    context_object_name = 'companies'
    ordering = ['-id']

    permission_required = 'invoice_app.view_company'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(eik__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class CompaniesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'table_views/companies/companies_add.html'

    permission_required = 'invoice_app.add_company'

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            url = f"{next_url}?company={self.object.id}"
            return url
        return reverse_lazy('companies_view')

class CompaniesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_update.html'
    success_url = reverse_lazy('companies_view')

    permission_required = 'invoice_app.change_company'

class CompaniesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_delete.html'
    success_url = reverse_lazy('companies_view')

    permission_required = 'invoice_app.delete_company'

class CompaniesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_details.html'

    permission_required = 'invoice_app.view_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['company'] = self.get_object()

        return context

@permission_required('invoice_app.view_company')
def get_company_values(request, company_id):
    company = Company.objects.get(pk=company_id)

    return JsonResponse({
        'company_database_name': str(company),
        'id': str(company.id),
        'eik': company.eik,
        'dds': company.dds,
        'name': company.name,
        'address': company.address,
        'mol': company.mol,
        'recipient': company.recipient,
    })


class InvoicesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Invoice
    template_name = 'table_views/invoices/invoices.html'
    context_object_name = 'invoices'
    ordering = ['-id']

    permission_required = 'invoice_app.view_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class InvoicesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'table_views/invoices/invoices_add.html'
    success_url = reverse_lazy('invoices_view')

    permission_required = 'invoice_app.add_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class InvoicesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Invoice
    form_class = InvoiceUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoices_update.html'
    success_url = reverse_lazy('invoices_view')

    permission_required = 'invoice_app.change_invoice'

class InvoicesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Invoice
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoices_delete.html'
    success_url = reverse_lazy('invoices_view')

    permission_required = 'invoice_app.delete_invoice'

class InvoicesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Invoice
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoice_details.html'

    permission_required = 'invoice_app.view_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['invoice'] = self.get_object()
        context['order_products'] = OrderProduct.objects.all()

        return context

class InvoicesReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Invoice
    queryset = Invoice.objects.all()
    template_name = 'table_views/invoices/invoice_report.html'
    context_object_name = 'invoices'
    ordering = ['-id']

    permission_required = 'invoice_app.view_invoice'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = InvoiceReportFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        filtered_queryset = self.get_queryset()

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['filter_form'] = self.filterset.form

        context['total_invoices'] = filtered_queryset.count()

        active_invoices_counter = 0
        total_sum_with_dds = 0
        total_sum_without_dds = 0
        for invoice in filtered_queryset:
            if not invoice.cancelled:
                active_invoices_counter += 1
                total_sum_with_dds += invoice.whole_price_with_dds
                total_sum_without_dds += invoice.whole_price_without_dds
        total_dds = (total_sum_without_dds - total_sum_with_dds)*(-1)

        context['total_active_invoices'] = active_invoices_counter
        context['total_sum_with_dds'] = total_sum_with_dds
        context['total_sum_without_dds'] = total_sum_without_dds
        context['total_dds'] = total_dds


        return context