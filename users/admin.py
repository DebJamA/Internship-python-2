from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("email", "username", "first_name", "last_name", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ('Personal Info', {"fields": ("username", "first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "first_name", "last_name",
                "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

# register the new CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
