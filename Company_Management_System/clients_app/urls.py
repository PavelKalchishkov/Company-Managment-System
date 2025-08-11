from django.urls import path

from .views import ClientsView, ClientsCreateView, ClientsUpdateView, ClientsDeleteView, ClientsDetailView

urlpatterns = [
    path('view/', ClientsView.as_view(), name='clients_view'),
    path('create/', ClientsCreateView.as_view(), name='clients_create_view'),
    path('update/<int:pk>', ClientsUpdateView.as_view(), name='clients_update_view'),
    path('delete/<int:pk>', ClientsDeleteView.as_view(), name='clients_delete_view'),
    path('details/<int:pk>', ClientsDetailView.as_view(), name='clients_details_view'),
]