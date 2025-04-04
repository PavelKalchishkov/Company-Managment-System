from django.urls import path

from employees_app.views import EmployeesView, EmployeesCreateView, EmployeesUpdateView, EmployeesDeleteView

urlpatterns = [
    path('view/', EmployeesView.as_view(), name='employees_view'),
    path('create/', EmployeesCreateView.as_view(), name='employees_create_view'),
    path('update/<int:pk>/', EmployeesUpdateView.as_view(), name='employees_update_view'),
    path('delete/<int:pk>/', EmployeesDeleteView.as_view(), name='employees_delete_view'),
]