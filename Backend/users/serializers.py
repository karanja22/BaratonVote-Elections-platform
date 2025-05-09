from rest_framework import serializers
from .models import User
from .registry import Student
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer as SimpleJWTTokenRefreshSerializer


class TokenRefreshSerializer(SimpleJWTTokenRefreshSerializer):
    pass


class RegistrationSerializer(serializers.Serializer):
    student_id = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        student_id = data['student_id']
        email = data['email']

        try:
            student = Student.objects.get(student_id=student_id)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Incorrect ID or Password.")

        if student.email.strip().lower() != email.strip().lower():
            raise serializers.ValidationError("Incorrect ID or password")    

        if User.objects.filter(student_id=student_id).exists():
            raise serializers.ValidationError("User already registered.")

        data['student'] = student
        return data

    def create(self, validated_data):
        student = validated_data['student']
        user = User.objects.create_user(
            username=student.student_id,
            email=validated_data['email'],
            password=validated_data['password'],
            student_id=student.student_id,
            first_name=student.first_name,
            last_name=student.last_name,
            department=student.department.name, 
            year_of_study=student.year_of_study,
            tribe=student.tribe,
            gender=student.gender,
            role='voter'
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    student_id = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):

        student_id = attrs.get('student_id')
        if not student_id:
            raise serializers.ValidationError("Student ID is required.")

        attrs['username'] = attrs.get('student_id') 
        return super().validate(attrs)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        token['student_id'] = user.student_id
        return token