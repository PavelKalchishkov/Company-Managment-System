from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CompanyCreateForm, CompanyUpdateForm, InvoiceCreateForm, InvoiceUpdateForm, InvoiceReportFilter
from .models import Company, Invoice


class CompaniesView(ListView, LoginRequiredMixin):
    model = Company
    template_name = 'table_views/companies/companies.html'
    context_object_name = 'companies'
    ordering = ['-id']

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

class CompaniesCreateView(CreateView, LoginRequiredMixin):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'table_views/companies/companies_add.html'

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            url = f"{next_url}?company={self.object.id}"
            return url
        return reverse_lazy('companies_view')

class CompaniesUpdateView(UpdateView, LoginRequiredMixin):
    model = Company
    form_class = CompanyUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_update.html'
    success_url = reverse_lazy('companies_view')

class CompaniesDeleteView(DeleteView, LoginRequiredMixin):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_delete.html'
    success_url = reverse_lazy('companies_view')

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


class InvoicesView(ListView, LoginRequiredMixin):
    model = Invoice
    template_name = 'table_views/invoices/invoices.html'
    context_object_name = 'invoices'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class InvoicesCreateView(CreateView, LoginRequiredMixin):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'table_views/invoices/invoices_add.html'
    success_url = reverse_lazy('invoices_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class InvoicesUpdateView(UpdateView, LoginRequiredMixin):
    model = Invoice
    form_class = InvoiceUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoices_update.html'
    success_url = reverse_lazy('invoices_view')

class InvoicesDeleteView(DeleteView, LoginRequiredMixin):
    model = Invoice
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoices_delete.html'
    success_url = reverse_lazy('invoices_view')

class InvoicesReportView(ListView, LoginRequiredMixin):
    model = Invoice
    queryset = Invoice.objects.all()
    template_name = 'table_views/invoices/invoice_report.html'
    context_object_name = 'invoices'

    ordering = ['-id']

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