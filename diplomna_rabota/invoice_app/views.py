from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CompanyCreateForm, CompanyUpdateForm
from .models import Company


class CompaniesView(ListView, LoginRequiredMixin):
    model = Company
    template_name = 'table_views/companies/companies.html'
    context_object_name = 'companies'

    ordering = ['-id']

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
    success_url = reverse_lazy('companies_view')

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

