from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model  # Importing get_user_model for compatibility
from django.db.models import Q

class StudentIDAuthBackend(BaseBackend):
    def authenticate(self, request, student_id=None, password=None, **kwargs):
        try:
            # Use get_user_model to ensure compatibility with custom user models
            User = get_user_model()  # Fetch the user model dynamically
            user = User.objects.get(Q(student_id=student_id))  # Fetch the user by student_id
            if user.check_password(password):  # Check if the password is correct
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            # Use get_user_model here as well
            User = get_user_model()
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
