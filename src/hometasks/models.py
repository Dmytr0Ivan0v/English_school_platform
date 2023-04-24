from django.db import models
from groups.models import Group


class Hometask(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="hometasks")
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.group}"
