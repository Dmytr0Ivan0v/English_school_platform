from django.contrib import admin
from hometasks.models import Hometask


@admin.register(Hometask)
class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    list_display = ["group", "title", "created_at"]
    list_filter = ["group"]
    search_fields = ["group"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("title",)}
