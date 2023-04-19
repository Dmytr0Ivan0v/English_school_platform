# Generated by Django 4.1.8 on 2023-04-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=20)),
                ("is_intetics", models.CharField(choices=[("Yes", "Yes"), ("No", "NO")], default="Yes", max_length=3)),
            ],
        ),
    ]
