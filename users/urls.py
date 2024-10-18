from django.urls import path
from .views import UserRegisterView, CustomTokenObtainPairView, UserListView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user-list'),  # List all users
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve, update, or delete a user
]
