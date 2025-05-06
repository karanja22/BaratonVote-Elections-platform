
from django.urls import path
from .views import RegistrationView, CustomTokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]