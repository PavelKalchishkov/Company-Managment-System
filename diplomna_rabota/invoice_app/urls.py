from django.urls import path

from .views import CompaniesView, CompaniesCreateView, CompaniesUpdateView, CompaniesDeleteView, InvoicesView, \
    InvoicesCreateView, InvoicesUpdateView, InvoicesDeleteView, get_company_values, InvoicesReportView

urlpatterns = [
    path('companies/view/', CompaniesView.as_view(), name='companies_view'),
    path('companies/create/', CompaniesCreateView.as_view(), name='companies_add_view'),
    path('companies/update/<int:pk>', CompaniesUpdateView.as_view(), name='companies_update_view'),
    path('companies/delete/<int:pk>', CompaniesDeleteView.as_view(), name='companies_delete_view'),
    path('companies/get-company-values/<int:company_id>', get_company_values, name='get_company_values'),
    path('view/', InvoicesView.as_view(), name='invoices_view'),
    path('create/', InvoicesCreateView.as_view(), name='invoices_add_view'),
    path('update/<int:pk>', InvoicesUpdateView.as_view(), name='invoices_update_view'),
    path('delete/<int:pk>', InvoicesDeleteView.as_view(), name='invoices_delete_view'),
    path('reports/', InvoicesReportView.as_view(), name='invoices_report_view'),
]