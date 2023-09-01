from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of username.
    """
    def create_user(self, uid, email, username, first_name, last_name, password, **extra_fields):
        """
        Create and save a user with the given email, names and password.
        """
        if not email:
            raise ValueError(_("The Email must be entered"))
        email = self.normalize_email(email)
        user = self.model(
            uid=uid,
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, uid, email, username, first_name, last_name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email, names and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(uid, email, username, first_name, last_name, password, **extra_fields)

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)
