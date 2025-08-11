from django.urls import path

from orders_app.views import OrdersView, OrdersCreateView, OrdersUpdateView, OrdersDeleteView, get_order_details, \
    get_order_values, OrdersDetailView

urlpatterns = [
    path('view/', OrdersView.as_view(), name='orders_view'),
    path('create/', OrdersCreateView.as_view(), name='orders_create_view'),
    path('update/<int:pk>/', OrdersUpdateView.as_view(), name='orders_update_view'),
    path('delete/<int:pk>/', OrdersDeleteView.as_view(), name='orders_delete_view'),
    path('details/<int:pk>/', OrdersDetailView.as_view(), name='orders_details_view'),
    path('get-order/<int:order_id>/', get_order_details, name='get_order_details'),
    path('get-order-values/<int:order_id>/', get_order_values, name='get_order_values'),
]