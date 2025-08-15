from django.urls import path
from .views import UserRegisterView, UserLoginView, logout_view, UserProfileDetailsViews, UserProfileUpdateView, \
    UserProfileDeleteView, change_password, change_password_done

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile_details/', UserProfileDetailsViews.as_view(), name='profile_details'),
    path('profile_edit/', UserProfileUpdateView.as_view(), name='profile_edit'),
    path('profile_delete/', UserProfileDeleteView.as_view(), name='profile_delete'),
    path('password_change/', change_password, name='password_change'),
    path('password_change/done/', change_password_done, name='password_change_done'),
]