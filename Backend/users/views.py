from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as SimpleJWTTokenRefreshView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import get_user_model



class RegistrationView(generics.CreateAPIView):
    User = get_user_model()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TokenRefreshView(SimpleJWTTokenRefreshView):
    serializer_class = TokenRefreshSerializer


@api_view(['POST'])
def login_view(request):
    student_id = request.data.get('student_id')
    password = request.data.get('password')

    if not student_id or not password:
        return Response({"detail": "Student ID and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = get_user_model().objects.get(student_id=student_id)
    except get_user_model().DoesNotExist:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

    if user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "Login successful",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })
    else:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)