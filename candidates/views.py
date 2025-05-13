from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import CandidateApplication
from .delegates import DelegateApplication
from .serializers import CandidateApplicationSerializer, DelegateApplicationSerializer


class ApplicationCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_context(self):
        return {'request': self.request}

    def check_student_application(self, model, user):
        if not user.student:
            raise ValidationError("Your student profile is incomplete. Please contact admin.")
        return model.objects.filter(student=user.student).exists()



class CandidateApplicationCreateView(ApplicationCreateView):
    serializer_class = CandidateApplicationSerializer

    def create(self, validated_data):
        user = self.request.user
        if self.check_student_application(CandidateApplication, user):
            raise ValidationError("You have already applied for a candidate position.")
        
        application = CandidateApplication.objects.create(student=user.student, **validated_data)
        application.check_eligibility()
        return application


class CandidateApplicationDetailView(generics.RetrieveAPIView):
    serializer_class = CandidateApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return CandidateApplication.objects.get(student=self.request.user.student)


class DelegateApplicationCreateView(ApplicationCreateView):
    serializer_class = DelegateApplicationSerializer

    def create(self, validated_data):
        user = self.request.user
        if self.check_student_application(DelegateApplication, user):
            raise ValidationError("You have already applied to be a delegate.")
        
        application = DelegateApplication.objects.create(student=user.student, **validated_data)
        application.check_eligibility()
        return application


class DelegateApplicationDetailView(generics.RetrieveAPIView):
    serializer_class = DelegateApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return DelegateApplication.objects.get(student=self.request.user.student)
