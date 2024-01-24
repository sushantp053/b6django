# Generated by Django 5.0 on 2024-01-24 05:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.IntegerField(primary_key=True, serialize=False)),
                ("image", models.ImageField(upload_to="")),
                ("text", models.TextField()),
                ("posted_at", models.DateTimeField()),
                ("location", models.TextField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                ("like_id", models.IntegerField(primary_key=True, serialize=False)),
                ("liked_at", models.DateTimeField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.post"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                ("comment_id", models.IntegerField(primary_key=True, serialize=False)),
                ("comment", models.TextField()),
                ("commented_at", models.DateTimeField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.post"
                    ),
                ),
            ],
        ),
    ]
