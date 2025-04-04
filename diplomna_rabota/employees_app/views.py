from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import EmployeeCreateForm, EmployeeUpdateForm
from .models import Employee


class EmployeesView(ListView, LoginRequiredMixin):
    model = Employee
    template_name = 'table_views/employees/employees.html'
    context_object_name = 'employees'

    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class EmployeesCreateView(CreateView, LoginRequiredMixin):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'table_views/employees/employees_add.html'
    success_url = reverse_lazy('employees_view')

class EmployeesUpdateView(UpdateView, LoginRequiredMixin):
    model = Employee
    form_class = EmployeeUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/employees/employees_update.html'
    success_url = reverse_lazy('employees_view')

class EmployeesDeleteView(DeleteView, LoginRequiredMixin):
    model = Employee
    pk_url_kwarg = 'pk'
    template_name = 'table_views/employees/employees_delete.html'
    success_url = reverse_lazy('employees_view')


