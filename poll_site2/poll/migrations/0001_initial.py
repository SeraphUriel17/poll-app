# Generated by Django 4.1 on 2022-08-27 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0002_alter_profile_phone_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("option_one", models.CharField(max_length=30)),
                ("option_two", models.CharField(max_length=30)),
                ("option_three", models.CharField(max_length=30)),
                ("option_four", models.CharField(max_length=30)),
                ("option_one_count", models.IntegerField(default=0)),
                ("option_two_count", models.IntegerField(default=0)),
                ("option_three_count", models.IntegerField(default=0)),
                ("option_four_count", models.IntegerField(default=0)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.profile",
                    ),
                ),
            ],
        ),
    ]
