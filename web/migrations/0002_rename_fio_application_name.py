# Generated by Django 5.0.7 on 2024-08-07 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="application",
            old_name="fio",
            new_name="name",
        ),
    ]