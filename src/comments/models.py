from django.conf import settings
from django.db import models
from hometasks.models import Hometask


class Comment(models.Model):
    hometask = models.ForeignKey(Hometask, on_delete=models.CASCADE, related_name="comments", null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments", null=False)
    prev_comment = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="next")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.hometask} - {self.user}"
