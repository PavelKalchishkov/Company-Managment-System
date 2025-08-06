from django.urls import path

from shippers_app.views import ShippersView, ShippersAddView, ShippersUpdateView, ShippersDeleteView, ShippersDetailView

urlpatterns = [
    path('view/', ShippersView.as_view(), name='shippers_view'),
    path('create/', ShippersAddView.as_view(), name='shippers_add_view'),
    path('update/<int:pk>/', ShippersUpdateView.as_view(), name='shippers_update_view'),
    path('delete/<int:pk>/', ShippersDeleteView.as_view(), name='shippers_delete_view'),
    path('details/<int:pk>/', ShippersDetailView.as_view(), name='shippers_details_view'),
]