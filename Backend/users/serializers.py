# users/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role', 'student_id', 'first_name' ,'last_name', 'department', 'gpa','year_of_study', 'tribe', 'gender']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash password using Argon2
        user.save()
        return user