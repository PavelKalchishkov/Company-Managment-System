from django.views.generic import TemplateView
from orders_app.models import Order
from products_app.models import Product
from employees_app.models import Employee
from clients_app.models import Client
from shippers_app.models import Shipper
from vendors_app.models import Vendor
from invoice_app.models import Invoice, Company
from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['username'] = user.username

        today = date.today()
        context['total_orders'] = Order.objects.all().count()
        context['new_orders_this_month'] = Order.objects.filter(
            order_date__year=today.year, order_date__month=today.month).count()

        context['total_products'] = Product.objects.all().count()
        context['new_products_this_month'] = Product.objects.filter(
            created_at__year=today.year, created_at__month=today.month).count()

        context['total_employees'] = Employee.objects.all().count()
        context['new_employees_this_month'] = Employee.objects.filter(
            added_at__year=today.year, added_at__month=today.month).count()

        context['total_clients'] = Client.objects.all().count()
        context['new_clients_this_month'] = Client.objects.filter(
            added_at__year=today.year, added_at__month=today.month).count()

        context['total_shippers'] = Shipper.objects.all().count()
        context['new_shippers_this_month'] = Shipper.objects.filter(
            added_at__year=today.year, added_at__month=today.month).count()

        context['total_vendors'] = Vendor.objects.all().count()
        context['new_vendors_this_month'] = Vendor.objects.filter(
            added_at__year=today.year, added_at__month=today.month).count()

        context['total_companies'] = Company.objects.all().count()
        context['new_companies_this_month'] = Company.objects.filter(
            added_at__year=today.year, added_at__month=today.month).count()

        context['total_invoices'] = Invoice.objects.all().count()
        context['new_invoices_this_month'] = Invoice.objects.filter(
            date__year=today.year, date__month=today.month).count()

        labels = []
        data = []

        for i in range(11, -1, -1):
            month_date = today - timedelta(days=30 * i)
            month_name = month_date.strftime('%b %Y')
            labels.append(month_name)

            count = Order.objects.filter(
                order_date__year=month_date.year,
                order_date__month=month_date.month,
                order_status = 'delivered'
            ).count()
            data.append(count)

        context['labels'] = labels
        context['data'] = data

        context['recent_orders'] = Order.objects.all().order_by('-order_date')[:10]

        return context