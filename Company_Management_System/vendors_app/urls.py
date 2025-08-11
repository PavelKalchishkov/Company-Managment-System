from django.urls import include, path
from .views import VendorsView, VendorsAddView, VendorsUpdateView, VendorsDeleteView, VendorsDetailView

urlpatterns = [
    path('view/', VendorsView.as_view(), name='vendors_view'),
    path('create/', VendorsAddView.as_view(), name='vendors_add_view'),
    path('update/<int:pk>/', VendorsUpdateView.as_view(), name='vendors_update_view'),
    path('delete/<int:pk>/', VendorsDeleteView.as_view(), name='vendors_delete_view'),
    path('details/<int:pk>/', VendorsDetailView.as_view(), name='vendors_details_view'),
]