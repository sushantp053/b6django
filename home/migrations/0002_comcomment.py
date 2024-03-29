# Generated by Django 5.0 on 2024-01-25 05:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ComComment",
            fields=[
                ("comId", models.IntegerField(primary_key=True, serialize=False)),
                ("comment", models.TextField()),
                (
                    "comment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.comments"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
