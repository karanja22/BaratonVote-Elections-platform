from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    """
    Custom User model that extends the default Django User model.
    This allows for additional fields relevant to the application.
    """
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('voter', 'Voter'),
        ('candidate', 'Candidate'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='voter')
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    year_of_study = models.IntegerField()
    tribe = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])

    # Changed related names to avoid clashes
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return self.username  # Return username for better readability

class UserProfile(models.Model):
    """
    Model to store additional profile information for users.
    Linked to the CustomUser model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username 

class AuthenticationLog(models.Model):
    """
    Model to track user login attempts and their outcomes.
    Useful for auditing and security monitoring.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    success = models.BooleanField(default=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_time} - {'Successful' if self.success else 'Failed'}"



class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    year_of_study = models.IntegerField()
    tribe = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    class Meta:
        managed = False 
        db_table = 'students'