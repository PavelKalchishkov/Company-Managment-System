from django.urls import include, path
from .views import VendorsView

urlpatterns = [
    path('', VendorsView.as_view(), name='vendors_view'),
]