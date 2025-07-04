from django.urls import path

from .views import ProductsView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView

urlpatterns = [
    path('view/', ProductsView.as_view(), name = 'products_view'),
    path('create/', ProductsCreateView.as_view(), name = 'products_create_view'),
    path('update/<int:pk>', ProductsUpdateView.as_view(), name = 'products_update_view'),
    path('delete/<int:pk>', ProductsDeleteView.as_view(), name = 'products_delete_view'),
]