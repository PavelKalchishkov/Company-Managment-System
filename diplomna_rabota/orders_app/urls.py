from django.urls import path

from orders_app.views import OrdersView, OrdersCreateView, OrdersUpdateView, OrdersDeleteView, get_order_details

urlpatterns = [
    path('view/', OrdersView.as_view(), name='orders_view'),
    path('create/', OrdersCreateView.as_view(), name='orders_create_view'),
    path('update/<int:pk>', OrdersUpdateView.as_view(), name='orders_update_view'),
    path('delete/<int:pk>', OrdersDeleteView.as_view(), name='orders_delete_view'),
    path('get-order/<int:order_id>/', get_order_details, name='get_order_details'),
]