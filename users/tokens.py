# users/tokens.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    student_id = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        student_id = attrs.get('student_id')
        password = attrs.get('password')

        user = authenticate(username=student_id, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid student ID or password.")

        refresh = self.get_token(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'student_id': user.student_id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
            }
        }

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
