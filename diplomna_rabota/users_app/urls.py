from django.urls import path
from .views import UserRegisterView, UserLoginView, logout_view, UserProfileDetailsViews

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile_details/', UserProfileDetailsViews.as_view(), name='profile_details'),
]