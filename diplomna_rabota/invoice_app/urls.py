from django.urls import path

from .views import CompaniesView, CompaniesCreateView, CompaniesUpdateView, CompaniesDeleteView


urlpatterns = [
    path('companies/view/', CompaniesView.as_view(), name='companies_view'),
    path('companies/create/', CompaniesCreateView.as_view(), name='companies_add_view'),
    path('companies/update/<int:pk>', CompaniesUpdateView.as_view(), name='companies_update_view'),
    path('companies/delete/<int:pk>', CompaniesDeleteView.as_view(), name='companies_delete_view'),
]