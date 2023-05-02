from django.db import models

variables = [("Yes", "Yes"), ("No", "No")]


class Group(models.Model):
    name = models.CharField(max_length=20)
    is_company = models.CharField(max_length=3, choices=variables, default="Yes")

    def __str__(self) -> str:
        return self.name
