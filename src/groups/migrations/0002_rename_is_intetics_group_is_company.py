# Generated by Django 4.1.8 on 2023-05-02 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="group",
            old_name="is_intetics",
            new_name="is_company",
        ),
    ]