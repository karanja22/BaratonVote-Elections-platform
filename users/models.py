from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .registry import Student

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('voter', 'Voter'),
        ('candidate', 'Candidate'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='voter')
    student = models.OneToOneField('Student', on_delete=models.CASCADE, null=True,blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

    def __str__(self):
        return self.username  

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username 

class AuthenticationLog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    success = models.BooleanField(default=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_time} - {'Successful' if self.success else 'Failed'}"



