from django.urls import path

from .views import CompaniesView, CompaniesCreateView, CompaniesUpdateView, CompaniesDeleteView, InvoicesView, \
    InvoicesCreateView, InvoicesUpdateView, InvoicesDeleteView

urlpatterns = [
    path('companies/view/', CompaniesView.as_view(), name='companies_view'),
    path('companies/create/', CompaniesCreateView.as_view(), name='companies_add_view'),
    path('companies/update/<int:pk>', CompaniesUpdateView.as_view(), name='companies_update_view'),
    path('companies/delete/<int:pk>', CompaniesDeleteView.as_view(), name='companies_delete_view'),
    path('invoices/view/', InvoicesView.as_view(), name='invoices_view'),
    path('invoices/create/', InvoicesCreateView.as_view(), name='invoices_add_view'),
    path('invoices/update/<int:pk>', InvoicesUpdateView.as_view(), name='invoices_update_view'),
    path('invoices/delete/<int:pk>', InvoicesDeleteView.as_view(), name='invoices_delete_view'),
]