from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    uid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return f"{self.email}, {self.username}"
