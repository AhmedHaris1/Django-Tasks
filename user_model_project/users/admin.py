from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationFomr
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationFomr
    model = CustomUser

    list_display = ("email", "is_staff", "is_active", "date_joined")
    list_filter = ("email", "is_staff", "is_active", "is_superuser", "date_joined")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "groups", "user_permissions", )})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields":("email", "password1", "password2", "is_staff",
                      "is_active", "groups", "user_permissions",)
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)