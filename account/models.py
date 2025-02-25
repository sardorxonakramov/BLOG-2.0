from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils import timezone
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique = True)
    username = None
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField(null = True, blank = True)
    created_at = models.DateTimeField(default = timezone.now)
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_permissions", blank=True
    )
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
   