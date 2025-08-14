from decimal import Decimal

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import CompanyCreateForm, CompanyUpdateForm, InvoiceCreateForm, InvoiceUpdateForm, InvoiceReportFilter
from .models import Company, Invoice
from orders_app.models import OrderProduct, Order

from django.http import FileResponse, HttpResponse
import io
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class CompaniesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Company
    template_name = 'table_views/companies/companies.html'
    context_object_name = 'companies'
    ordering = ['-id']

    permission_required = 'invoice_app.view_company'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(eik__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class CompaniesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'table_views/companies/companies_add.html'

    permission_required = 'invoice_app.add_company'

    def get_success_url(self):
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            url = f"{next_url}?company={self.object.id}"
            return url
        return reverse_lazy('companies_view')

class CompaniesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_update.html'
    success_url = reverse_lazy('companies_view')

    permission_required = 'invoice_app.change_company'

class CompaniesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_delete.html'
    success_url = reverse_lazy('companies_view')

    permission_required = 'invoice_app.delete_company'

class CompaniesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = 'table_views/companies/companies_details.html'

    permission_required = 'invoice_app.view_company'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['company'] = self.get_object()

        return context

@permission_required('invoice_app.view_company')
def get_company_values(request, company_id):
    company = Company.objects.get(pk=company_id)

    return JsonResponse({
        'company_database_name': str(company),
        'id': str(company.id),
        'eik': company.eik,
        'dds': company.dds,
        'name': company.name,
        'address': company.address,
        'mol': company.mol,
        'recipient': company.recipient,
    })


class InvoicesView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Invoice
    template_name = 'table_views/invoices/invoices.html'
    context_object_name = 'invoices'
    ordering = ['-id']

    permission_required = 'invoice_app.view_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class InvoicesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'table_views/invoices/invoices_add.html'
    success_url = reverse_lazy('invoices_view')

    permission_required = 'invoice_app.add_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context

class InvoicesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Invoice
    form_class = InvoiceUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoices_update.html'
    success_url = reverse_lazy('invoices_view')

    permission_required = 'invoice_app.change_invoice'

class InvoicesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Invoice
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoices_delete.html'
    success_url = reverse_lazy('invoices_view')

    permission_required = 'invoice_app.delete_invoice'

class InvoicesDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Invoice
    pk_url_kwarg = 'pk'
    template_name = 'table_views/invoices/invoice_details.html'

    permission_required = 'invoice_app.view_invoice'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['invoice'] = self.get_object()
        context['order_products'] = OrderProduct.objects.all()

        return context

class InvoicesReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Invoice
    queryset = Invoice.objects.all()
    template_name = 'table_views/invoices/invoice_report.html'
    context_object_name = 'invoices'
    ordering = ['-id']

    permission_required = 'invoice_app.view_invoice'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = InvoiceReportFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        filtered_queryset = self.get_queryset()

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['filter_form'] = self.filterset.form

        context['total_invoices'] = filtered_queryset.count()

        active_invoices_counter = 0
        total_sum_with_dds = 0
        total_sum_without_dds = 0
        for invoice in filtered_queryset:
            if not invoice.cancelled:
                active_invoices_counter += 1
                total_sum_with_dds += invoice.whole_price_with_dds
                total_sum_without_dds += invoice.whole_price_without_dds
        total_dds = (total_sum_without_dds - total_sum_with_dds)*(-1)

        context['total_active_invoices'] = active_invoices_counter
        context['total_sum_with_dds'] = total_sum_with_dds
        context['total_sum_without_dds'] = total_sum_without_dds
        context['total_dds'] = total_dds

        return context


def generate_pdf(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    order_products = OrderProduct.objects.all()

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CenterTitle", alignment=1, fontSize=26, spaceAfter=24))
    styles.add(ParagraphStyle(name="CenterTitle2", alignment=1, fontSize=16, spaceAfter=16))
    styles.add(ParagraphStyle(name="CenterTitle3", alignment=1, fontSize=12, spaceAfter=4))
    styles.add(ParagraphStyle(name="CenterTitle4", alignment=1, fontSize=12, spaceAfter=16))

    elements = []

    elements.append(Paragraph("Invoice", styles["CenterTitle"]))
    elements.append(Paragraph(f"{invoice}", styles["CenterTitle2"]))
    elements.append(Paragraph(f"Date of issue", styles["CenterTitle3"]))
    elements.append(Paragraph(f"{invoice.date}", styles["CenterTitle4"]))

    # Supplier and Recipient Info
    recipient_company_info = [
        ["Recipient", invoice.company.recipient],
        ["Company", invoice.company.name],
        ["EIK", invoice.company.eik],
        ["Address", Paragraph(invoice.company.address, styles["Normal"])],
        ["MOL", invoice.company.mol],
        ["DDS", invoice.company.dds],
    ]

    supplier_company_info = [
        ["Supplier", "Pavel Kalchishkov"],
        ["Company", "Technocenter OOD"],
        ["EIK", "1111111111"],
        ["Address", "Goce Delchev 30"],
        ["Mol", "Pavel Kalchishkov"],
        ["DDS", "BG111111111"]
    ]

    recipient_company_table = Table(recipient_company_info, colWidths=[100, 150])
    recipient_company_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ]))

    supplier_company_table = Table(supplier_company_info, colWidths=[100, 150])
    supplier_company_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ]))

    info_table = Table([
        [recipient_company_table, supplier_company_table]
    ])
    elements.append(info_table)
    elements.append(Spacer(1, 12))

    order_details = [
        ["Order", invoice.order],
        ["Raw Price", invoice.order.order_price],
        ["Payment Method", invoice.order.payment_method],
        ["Status", invoice.order.order_status],
        ["Client", invoice.order.client],
        ["Employee", invoice.order.employee],
        ["Shipper", invoice.order.shipper],
    ]

    invoice_details = [
        ["Invoice", invoice],
        ["DDS(%)", invoice.DDS],
        ["Date", invoice.date],
        ["Discount", invoice.discount],
        ["Status", "Active" if not invoice.cancelled else "Cancelled"],
        ["-","-"],
        ["-", "-"]
    ]

    order_details_table = Table(order_details, colWidths=[100, 150])
    invoice_details_table = Table(invoice_details, colWidths=[100, 150])

    order_details_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ]))

    invoice_details_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ]))

    info_table_2 = Table([
        [order_details_table, invoice_details_table],
    ])
    elements.append(info_table_2)
    elements.append(Spacer(1, 12))

    # Products Table
    product_data = [["Products", "Quantity", "Unit Price", "Total"]]

    for order_product in order_products:
        if invoice.order.id == order_product.order_id:
            product_data.append([order_product.product.name, order_product.quantity, order_product.product.price, order_product.product.price * order_product.quantity])

    products_table = Table(product_data, colWidths=[255, 84, 86, 86])
    products_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("ALIGN", (1, 1), (-1, -1), "CENTER"),
    ]))
    elements.append(products_table)
    elements.append(Spacer(1, 12))

    # Totals
    discount_no_dds = invoice.whole_price_without_dds * invoice.discount * Decimal(0.01)
    discount_with_dds = invoice.whole_price_with_dds * invoice.discount * Decimal(0.01)


    totals_data = [
        ["Price", "Leva"],
        ["Whole Price (No DDS)", f"{invoice.whole_price_without_dds:.2f} lv"],
        ["Whole Price (With DDS)", f"{invoice.whole_price_with_dds:.2f} lv"],
        ["Discount (No DDS)", f"{discount_no_dds:.2f} lv"],
        ["Discount (With DDS)", f"{discount_with_dds:.2f} lv"],
    ]
    totals_table = Table(totals_data, colWidths=[255, 255])
    totals_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ]))
    elements.append(totals_table)
    elements.append(Spacer(1, 50))

    signature_data = [
        [
            Paragraph("Received the invoice:<br/>Signature: ____________", styles["Normal"]),
            "",  # Empty column for spacing
            Paragraph("Issued the invoice:<br/>Signature: ____________", styles["Normal"])
        ]
    ]

    signature_table = Table(signature_data, colWidths=[200, 70, 200], hAlign="CENTER")
    signature_table.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 30),  # space above
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
    ]))
    elements.append(signature_table)


    doc.build(elements)

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"invoice_{invoice}.pdf")


