from rest_framework import serializers
from .models import CandidateApplication
from .delegates import DelegateApplication


class CandidateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateApplication
        fields = ['position_applied', 'manifesto', 'application_status', 'eligible', 'submission_date']
        read_only_fields = ['application_status', 'eligible', 'submission_date']

    def create(self, validated_data):
        user = self.context['request'].user
        student = user.student  # Assuming you have a student relationship attached to User
        
        # Check if a candidate application already exists for the student
        if CandidateApplication.objects.filter(student=student).exists():
            raise serializers.ValidationError("You have already applied for a candidate position.")

        # Create application and check eligibility
        application = CandidateApplication.objects.create(student=student, **validated_data)
        application.check_eligibility()
        return application


class DelegateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelegateApplication
        fields = ['on_work_study', 'department', 'application_status', 'eligible', 'submission_date']
        read_only_fields = ['application_status', 'eligible', 'submission_date']

    def create(self, validated_data):
        user = self.context['request'].user
        student = user.student  # Assuming you have a student relationship attached to User

        # Check if a delegate application already exists for the student
        if DelegateApplication.objects.filter(student=student).exists():
            raise serializers.ValidationError("You have already applied to be a delegate.")

        # Create application and check eligibility
        application = DelegateApplication.objects.create(student=student, **validated_data)
        application.check_eligibility()
        return application
