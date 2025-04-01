from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Vendor


class VendorsView(LoginRequiredMixin, ListView):
    model = Vendor
    template_name = 'table_views/vendors/vendors.html'
    context_object_name = 'vendors'

    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['user_authenticated'] = user.is_authenticated
        context['user'] = user
        return context


