from comments.models import Comment
from django.contrib import admin

FIELDS = ["hometask", "student"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = FIELDS
    search_fields = FIELDS
    list_filter = FIELDS
    ordering = ["-created_at"]
