from django.urls import path  
from .views import RegistrationView, CustomTokenObtainPairView, TokenRefreshView, login_view  

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', login_view, name='login'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
