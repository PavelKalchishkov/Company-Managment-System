from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import EmployeeCreateForm, EmployeeUpdateForm
from .models import Employee


class EmployeesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Employee
    template_name = 'table_views/employees/employees.html'
    context_object_name = 'employees'

    ordering = ['-id']

    permission_required = 'employees_app.view_employee'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            terms = query.strip().split()

            if len(terms) == 1:
                queryset = queryset.filter(
                    Q(first_name__icontains=terms[0]) |
                    Q(last_name__icontains=terms[0]) |
                    Q(phone_number__icontains=terms[0])
                )

            elif len(terms) >= 2:
                queryset = queryset.filter(
                    (Q(first_name__icontains=terms[0]) & Q(last_name__icontains=terms[1])) |
                    (Q(first_name__icontains=terms[1]) & Q(last_name__icontains=terms[0])) |
                    Q(phone_number__icontains=query)
                )
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class EmployeesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'table_views/employees/employees_add.html'
    success_url = reverse_lazy('employees_view')

    permission_required = 'employees_app.add_employee'

class EmployeesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/employees/employees_update.html'
    success_url = reverse_lazy('employees_view')

    permission_required = 'employees_app.change_employee'

class EmployeesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Employee
    pk_url_kwarg = 'pk'
    template_name = 'table_views/employees/employees_delete.html'
    success_url = reverse_lazy('employees_view')

    permission_required = 'employees_app.delete_employee'

class EmployeesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Employee
    pk_url_kwarg = 'pk'
    template_name = 'table_views/employees/employees_details.html'

    permission_required = 'employees_app.view_employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['employee'] = self.get_object()

        return context


