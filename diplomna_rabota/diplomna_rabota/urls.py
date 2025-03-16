from django.contrib import admin
from django.urls import path, include
from diplomna_rabota import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('user/', include('users_app.urls')),
]
