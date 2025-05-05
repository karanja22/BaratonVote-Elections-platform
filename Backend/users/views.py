from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import User
from .serializers import UserSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Baraton Vote Elections Platform!")

class CustomTokenObtainPairView(TokenObtainPairView):
    # Optionally override this view to customize token response
    pass

class TokenRefreshView(TokenRefreshView):
    pass
