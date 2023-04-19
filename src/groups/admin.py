from django.contrib import admin
from groups.models import Group

FIELDS = ["name", "is_intetics"]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = FIELDS
    list_filter = FIELDS
    search_fields = FIELDS
