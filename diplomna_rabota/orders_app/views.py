from decimal import Decimal
from django.http import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import DecimalField
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.functional import cached_property
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import OrderProduct

from .forms import OrderCreationForm, OrderUpdateForm, OrderProductForm, OrderViewFilter
from .models import Order


class OrdersView(ListView, LoginRequiredMixin):
    model = Order
    template_name = 'table_views/orders/orders.html'
    context_object_name = 'orders'
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = OrderViewFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        context['order_products'] = OrderProduct.objects.all()
        context['filter_form'] = self.filterset.form
        return context


OrderProductFormSet = inlineformset_factory(
    Order, OrderProduct, form=OrderProductForm, extra=1, can_delete=True
)

class OrdersCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderCreationForm
    template_name = 'table_views/orders/orders_add.html'

    @cached_property
    def formset_class(self):
        extra_forms = int(self.request.GET.get('product_count', 1))  # Default 1 row
        return inlineformset_factory(
            Order,
            OrderProduct,
            form=OrderProductForm,
            extra=extra_forms,
            can_delete=False
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = self.formset_class(self.request.POST)
        else:
            context['formset'] = self.formset_class()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            order = self.object
            for order_product in order.orderproduct_set.all():
                quantity = order_product.quantity
                product_price = order_product.product.price
                order.order_price += Decimal(product_price) * quantity

            order.save()

            next_url = self.request.POST.get('next') or self.request.GET.get('next')
            if next_url:
                url = f"{next_url}?order={self.object.id}"
                return redirect(url)
            return redirect(reverse_lazy('orders_view'))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class OrdersUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'table_views/orders/orders_update.html'
    success_url = reverse_lazy('orders_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()

        OrderProductFormSet = inlineformset_factory(
            Order, OrderProduct, form=OrderProductForm, extra=0, can_delete=True
        )

        if self.request.method == 'POST':
            context['formset'] = OrderProductFormSet(self.request.POST, instance=order)
        else:
            context['formset'] = OrderProductFormSet(instance=order)

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            order = self.get_object()
            order.order_version += 1
            order.order_price = Decimal(0)
            for order_product in order.orderproduct_set.all():
                quantity = order_product.quantity
                product_price = order_product.product.price
                order.order_price += Decimal(product_price) * quantity

            order.save()

            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class OrdersDeleteView(DeleteView, LoginRequiredMixin):
    model = Order
    pk_url_kwarg = 'pk'
    template_name = 'table_views/orders/orders_delete.html'
    success_url = reverse_lazy('orders_view')


def get_order_details(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        return JsonResponse({'price': float(order.order_price)})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)

def get_order_values(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)

        products_data = []
        for order_product in OrderProduct.objects.filter(order=order).select_related('product'):
            product = order_product.product
            products_data.append(
                f'product_id: {product.id}|product_name: {product.name}|quantity: {order_product.quantity}')

        return JsonResponse({
            'id': str(order.id),
            'date': order.order_date,
            'address': order.order_address,
            'version': order.order_version,
            'price': float(order.order_price),
            'payment_method': order.payment_method,
            'status': order.order_status,
            'client': str(order.client),
            'employee': str(order.employee),
            'shipper': str(order.shipper),
            'products': products_data,
        })

    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
