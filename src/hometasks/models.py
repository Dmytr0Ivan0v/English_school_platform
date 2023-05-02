from django.db import models
from django.urls import reverse
from groups.models import Group


class Hometask(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="hometasks")
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique_for_date="created_at")

    def __str__(self) -> str:
        return f"{self.title} - {self.group}"

    def get_absolute_url(self):
        return reverse(
            "hometask:hometask_retrieve",
            args=[
                self.created_at.year,
                self.created_at.month,
                self.created_at.day,
                self.slug,
            ],
        )
