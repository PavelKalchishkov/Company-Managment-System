from django.contrib import admin
from django.urls import path, include
from diplomna_rabota import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/', include('users_app.urls')),
    path('vendors/', include('vendors_app.urls')),
    path('shippers/', include('shippers_app.urls')),
    path('products/', include('products_app.urls')),
    path('employees/', include('employees_app.urls')),
    path('clients/', include('clients_app.urls')),
    path('orders/', include('orders_app.urls')),
]
