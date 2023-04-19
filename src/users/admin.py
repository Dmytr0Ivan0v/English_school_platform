from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ("user_permissions", "groups")
    readonly_fields = (
        # "email",
        "password",
        "last_login",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    list_display = ("first_name", "last_name", "email", "group", "role")
    list_filter = ("group", "first_name", "role")
    search_fields = ("group", "first_name", "role")
